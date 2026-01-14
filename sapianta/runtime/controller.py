from sapianta.governance.interface.interface import GovernanceInterface
from sapianta.governance.interface.types import GovernanceRequest
from sapianta.governance.roi.interface import ROIInterface
from sapianta.governance.roi.types import ROIContext
from sapianta.runtime.trace.types import RuntimeTraceRecord
from sapianta.runtime.trace.console import ConsoleTraceSink
from .types import RuntimeDecision, RuntimeResult


class RuntimeController:
    """
    Runtime Controller:
    - kliče Governance Interface
    - kliče ROI Interface
    - odloči, ali se tok nadaljuje
    - ne izvaja nobenih akcij
    - F36: emitira read-only runtime trace
    """

    def __init__(self, roi_interface: ROIInterface):
        self.roi_interface = roi_interface
        self.trace_sink = ConsoleTraceSink()

    def process(self, request: GovernanceRequest, roi_context: ROIContext) -> RuntimeResult:
        # 1️⃣ Governance → Core
        governance_response = GovernanceInterface.handle(request)
        core_response = governance_response.core_response

        # 2️⃣ Če Core zavrne → takoj HALT
        if core_response.status.value != "ACCEPTED":
            self.trace_sink.emit(
                RuntimeTraceRecord(
                    decision=RuntimeDecision.HALT,
                    reason="CORE_REJECTED",
                    source="RuntimeController"
                )
            )
            return RuntimeResult(
                decision=RuntimeDecision.HALT,
                core_response=core_response,
                reason="CORE_REJECTED"
            )

        # 3️⃣ ROI evalvacija
        roi_result = self.roi_interface.evaluate(core_response, roi_context)

        if not roi_result.allowed:
            self.trace_sink.emit(
                RuntimeTraceRecord(
                    decision=RuntimeDecision.HALT,
                    reason="ROI_BLOCKED",
                    source="RuntimeController"
                )
            )
            return RuntimeResult(
                decision=RuntimeDecision.HALT,
                core_response=core_response,
                roi_result=roi_result,
                reason="ROI_BLOCKED"
            )

        # 4️⃣ Če vse pusti → PROCEED (execution še NE obstaja)
        self.trace_sink.emit(
            RuntimeTraceRecord(
                decision=RuntimeDecision.PROCEED,
                reason=None,
                source="RuntimeController"
            )
        )
        return RuntimeResult(
            decision=RuntimeDecision.PROCEED,
            core_response=core_response,
            roi_result=roi_result
        )

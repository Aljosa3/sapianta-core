from runtime.layer2.audit_trace_collector import AuditTraceCollector


def test_audit_trace_structure():
    collector = AuditTraceCollector()

    trace = collector.collect(
        event_id="E1",
        previous_state=1,
        new_state=2,
        allowed=True,
    )

    assert trace["event_id"] == "E1"
    assert trace["allowed"] is True
    assert trace["previous_state"] == 1
    assert trace["new_state"] == 2

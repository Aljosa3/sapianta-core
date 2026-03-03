from abc import ABC, abstractmethod


class DomainPolicy(ABC):
    """
    Domain-agnostic execution contract.

    Any domain (trading, credit, risk, AI, etc.)
    must implement this interface to integrate
    with the ExecutionBoundary layer.
    """

    POLICY_NAME: str
    POLICY_VERSION: str

    @abstractmethod
    def execute(self, input_data, config, t=None):
        """
        Domain-agnostic execution interface.

        Parameters
        ----------
        input_data:
            - trading: full market data dict
            - credit: single application
            - other domains: domain-specific payload

        config:
            Frozen deterministic config snapshot

        t:
            Optional index/time step for sequential domains

        Returns
        -------
        Domain-specific deterministic result.
        Must not mutate engine state.
        """
        pass
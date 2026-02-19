class ControlLayerError(Exception):
    """Base class for Layer 2 deterministic failures."""
    pass


class PolicyDeniedError(ControlLayerError):
    """Raised when policy evaluation denies execution."""
    pass


class ContractViolationError(ControlLayerError):
    """Raised when TransitionContract validation fails."""
    pass


class PreInvariantViolationError(ControlLayerError):
    """Raised when pre-transition invariant fails."""
    pass


class PostInvariantViolationError(ControlLayerError):
    """Raised when post-transition invariant fails."""
    pass

class StateMutationError(ControlLayerError):
    """Raised when in-place state mutation is detected."""
    pass

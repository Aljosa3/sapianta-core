class CLIError(Exception):
    """Base class for all CLI errors."""
    pass


class InvalidCommandError(CLIError):
    """Raised when an unknown CLI command is invoked."""
    pass


class InvalidArgumentsError(CLIError):
    """Raised when CLI arguments are malformed or incomplete."""
    pass

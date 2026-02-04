class TextNormalizationError(Exception):
    """Base exception for text normalization errors."""
    pass


class InvalidTextInputError(TextNormalizationError):
    """Raised when input is not a valid string."""
    pass

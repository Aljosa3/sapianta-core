class ModuleBuilderError(Exception):
    pass


class SchemaError(ModuleBuilderError):
    pass


class IGLValidationError(ModuleBuilderError):
    pass


class EmissionError(ModuleBuilderError):
    pass

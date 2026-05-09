def __getattr__(name):
    if name == "AzureImageTranslator":
        from co_op_translator.core.vision.providers.azure.image_translator import (
            AzureImageTranslator,
        )

        return AzureImageTranslator
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = []

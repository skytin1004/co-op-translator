from typing import Any


def estimate_translation_tokens(
    translation_manager: Any, update: bool = False
) -> dict[str, int]:
    """Return normalized token estimate breakdown from translation manager."""
    est = translation_manager.estimate_tokens(update=update)
    return {
        "markdown": int(est.get("markdown", 0) or 0),
        "notebook": int(est.get("notebook", 0) or 0),
        "images": int(est.get("images", 0) or 0),
        "outdated": int(est.get("outdated", 0) or 0),
        "total": int(est.get("total", 0) or 0),
    }

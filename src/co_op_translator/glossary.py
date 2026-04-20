from contextlib import contextmanager
from typing import Iterable, Iterator

_glossary_terms: list[str] = []


def normalize_glossary_terms(glossary_terms: Iterable[str] | None) -> list[str]:
    """Normalize glossary terms into a de-duplicated ordered list of strings."""
    if not glossary_terms:
        return []

    if isinstance(glossary_terms, str):
        glossary_terms = [glossary_terms]

    normalized: list[str] = []
    seen: set[str] = set()
    for term in glossary_terms:
        if term is None:
            continue
        text = str(term).strip()
        if not text or text in seen:
            continue
        normalized.append(text)
        seen.add(text)
    return normalized


def set_glossary_terms(glossary_terms: Iterable[str] | None) -> None:
    """Set the process-wide glossary terms used by prompt builders."""
    global _glossary_terms
    _glossary_terms = normalize_glossary_terms(glossary_terms)


def get_glossary_terms() -> list[str]:
    """Return the current process-wide glossary terms."""
    return list(_glossary_terms)


@contextmanager
def glossary_terms_scope(glossary_terms: Iterable[str] | None) -> Iterator[None]:
    """Temporarily set glossary terms for one translation API invocation."""
    previous_terms = get_glossary_terms()
    set_glossary_terms(glossary_terms)
    try:
        yield
    finally:
        set_glossary_terms(previous_terms)


def _build_glossary_lines() -> list[str]:
    terms = get_glossary_terms()
    if not terms:
        return []

    lines = [
        "GLOSSARY (do not translate or change these terms; keep them exactly as written):"
    ]
    lines.extend(f"- {term}" for term in terms)
    return lines


def inject_markdown_glossary(prompt: str, delimiter: str) -> str:
    """Inject glossary instructions into a markdown prompt if terms are configured."""
    glossary_lines = _build_glossary_lines()
    if not glossary_lines:
        return prompt

    glossary_block = "\n\n" + "\n".join(glossary_lines) + "\n"
    index = prompt.find(delimiter)
    if index == -1:
        return prompt + glossary_block
    prefix = prompt[:index]
    suffix = prompt[index:]
    return prefix + glossary_block + suffix


def build_image_glossary_block() -> str:
    """Return an image-prompt glossary block if terms are configured."""
    glossary_lines = _build_glossary_lines()
    if not glossary_lines:
        return ""
    return "\n".join(glossary_lines)

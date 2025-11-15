from typing import Iterable


_glossaries: list[str] = []
_patched = False


def set_glossaries(glossaries: Iterable[str] | None) -> None:
    global _glossaries
    _glossaries = _normalize_glossaries(glossaries)
    if _glossaries:
        _ensure_patched()


def get_glossaries() -> list[str]:
    return list(_glossaries)


def _normalize_glossaries(glossaries: Iterable[str] | None) -> list[str]:
    if not glossaries:
        return []
    normalized: list[str] = []
    for term in glossaries:
        if term is None:
            continue
        text = str(term).strip()
        if text:
            normalized.append(text)
    return normalized


def _ensure_patched() -> None:
    global _patched
    if _patched:
        return

    from co_op_translator.core.llm import markdown_translator, text_translator

    original_md_generate = markdown_translator.generate_prompt_template

    def generate_prompt_template_with_glossary(
        language_code: str,
        language_name: str,
        document_chunk: str,
        is_rtl: bool,
    ) -> str:
        prompt = original_md_generate(
            language_code,
            language_name,
            document_chunk,
            is_rtl,
        )
        return _inject_markdown_glossary(
            prompt,
            language_code,
            language_name,
        )

    def gen_image_translation_prompt_with_glossary(
        text_data,
        language_code,
        language_name,
    ):
        return _build_image_prompt_with_glossary(
            text_data,
            language_code,
            language_name,
        )

    markdown_translator.generate_prompt_template = (
        generate_prompt_template_with_glossary
    )
    text_translator.gen_image_translation_prompt = (
        gen_image_translation_prompt_with_glossary
    )

    _patched = True


def _build_markdown_glossary_block(
    language_code: str,
    language_name: str,
) -> str:
    if not _glossaries:
        return ""
    lines: list[str] = []
    lines.append(
        "\n\nGLOSSARY (do not translate or change these terms; keep them exactly as written):\n"
    )
    for term in _glossaries:
        lines.append(f"- {term}\n")
    return "".join(lines)


def _inject_markdown_glossary(
    prompt: str,
    language_code: str,
    language_name: str,
) -> str:
    if not _glossaries:
        return prompt

    from co_op_translator.utils.llm import markdown_utils

    block = _build_markdown_glossary_block(language_code, language_name)
    if not block:
        return prompt

    delimiter = markdown_utils.SPLIT_DELIMITER
    index = prompt.find(delimiter)
    if index == -1:
        return prompt + block
    prefix = prompt[:index]
    suffix = prompt[index:]
    return prefix + block + suffix


def _build_image_prompt_with_glossary(
    text_data,
    language_code,
    language_name,
) -> str:
    header = (
        f"Translate each line to {language_name} ({language_code}). "
        "Keep exact same number of lines and preserve original formatting."
    )
    parts: list[str] = [header, ""]
    if _glossaries:
        parts.append(
            "GLOSSARY (do not translate or change these terms; keep them exactly as written):"
        )
        for term in _glossaries:
            parts.append(f"- {term}")
        parts.append("")
    for line in text_data or []:
        parts.append(str(line))
    prompt = "\n".join(parts)
    if text_data:
        prompt += "\n"
    return prompt

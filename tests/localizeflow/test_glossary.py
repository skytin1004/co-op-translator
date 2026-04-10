from co_op_translator.localizeflow.glossary import set_glossaries
from co_op_translator.core.llm import markdown_translator, text_translator


def test_markdown_prompt_includes_glossary_before_content():
    try:
        set_glossaries(["Co-op Translator"])
        chunk = "Hello Co-op Translator."
        prompt = markdown_translator.generate_prompt_template(
            "ko",
            "Korean",
            chunk,
            is_rtl=False,
        )
        delimiter = markdown_translator.SPLIT_DELIMITER
        assert delimiter in prompt
        before, after = prompt.split(delimiter, 1)
        assert "GLOSSARY" in before
        assert "Co-op Translator" in before
        assert chunk in after
    finally:
        set_glossaries([])


def test_image_prompt_includes_glossary():
    try:
        set_glossaries(["Co-op Translator"])
        text_data = ["Co-op Translator Cloud"]
        prompt = text_translator.gen_image_translation_prompt(
            text_data,
            "ko",
            "Korean",
        )
        assert "GLOSSARY" in prompt
        assert "Co-op Translator" in prompt
        for line in text_data:
            assert line in prompt
    finally:
        set_glossaries([])

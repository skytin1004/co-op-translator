"""Code block preservation helpers for markdown translation."""

from __future__ import annotations

from co_op_translator.utils.llm.chunking import _parse_markdown_text_and_code_parts


def replace_code_blocks(document: str):
    """
    Replace code blocks in the document with placeholders.
    Inline code is left as-is for the LLM to handle naturally.

    Args:
        document (str): The markdown document to process.

    Returns:
        tuple: A tuple containing:
            - The document with placeholders.
            - A dictionary mapping placeholders to their original code.
    """
    placeholder_map = {}

    parts = _parse_markdown_text_and_code_parts(document)

    output_segments = []
    code_index = 0
    for segment, seg_type in parts:
        if seg_type == "code":
            placeholder = f"@@CODE_BLOCK_{code_index}@@"
            output_segments.append(placeholder)
            placeholder_map[placeholder] = segment
            code_index += 1
        else:
            output_segments.append(segment)

    return "".join(output_segments), placeholder_map


def restore_code_blocks(translated_document: str, placeholder_map: dict) -> str:
    """
    Restore code blocks into the translated document from the placeholders.

    Args:
        translated_document (str): The translated document containing placeholders.
        placeholder_map (dict): A dictionary mapping placeholders to their original code.

    Returns:
        str: The translated document with the original code blocks restored.
    """
    for placeholder, code in placeholder_map.items():
        translated_document = translated_document.replace(placeholder, code)

    return translated_document


def extract_json_from_markdown_codeblock(response: str) -> str:
    """
    Extract JSON content from markdown code blocks.

    Extracts JSON formatted as markdown code blocks (```json) from LLM responses.

    Args:
        response (str): Original response text from the LLM

    Returns:
        str: Cleaned JSON string with markdown formatting removed
    """
    cleaned_response = response

    # Check if the response starts with a markdown code block
    if cleaned_response.strip().startswith("```"):
        # Extract content between the first and last code block markers
        parts = cleaned_response.split("```", 2)
        if len(parts) >= 3:
            # If the format is ```json\n{...}\n```, take the middle part
            json_content = parts[1]
            # Remove language identifier if present
            if "\n" in json_content:
                json_content = json_content.split("\n", 1)[1]
            cleaned_response = json_content
        else:
            # Handle cases where closing ``` might be missing
            if cleaned_response.strip().startswith("```json"):
                cleaned_response = cleaned_response.replace("```json", "", 1).strip()
            elif cleaned_response.strip().startswith("```"):
                cleaned_response = cleaned_response.replace("```", "", 1).strip()

    return cleaned_response

"""
This module contains utility functions for handling file operations.
Functions include reading from files, writing to files, and handling empty document scenarios.
"""

import hashlib
from pathlib import Path
import shutil
import os
import logging

logger = logging.getLogger(__name__)


def read_input_file(input_file: str | Path) -> str:
    """
    Read the content of an input file and return it as a stripped string.

    Args:
        input_file (str | Path): The path to the input file.

    Returns:
        str: The stripped content of the file.
    """
    input_file = Path(input_file)
    with input_file.open("r", encoding="utf-8") as file:
        return file.read().strip()


def handle_empty_document(input_file: str | Path, output_file: str | Path) -> None:
    """
    Copy the input file to the output location if the document is empty.

    Args:
        input_file (str | Path): The path to the input file.
        output_file (str | Path): The path to the output file.
    """
    input_file = Path(input_file)
    output_file = Path(output_file)
    shutil.copyfile(input_file, output_file)


def write_output_file(output_file: str | Path, results: list) -> None:
    """
    Write a list of results to the output file, each on a new line.

    Args:
        output_file (str | Path): The path to the output file.
        results (list): A list of strings to write to the file.
    """
    output_file = Path(output_file)
    # Create parent directories if they don't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open("w", encoding="utf-8") as file:
        file.write("\n".join(results))


def get_actual_image_path(
    image_relative_path: str | Path,
    markdown_file_path: str | Path,
    root_dir: Path = None,
) -> Path:
    """
    Given an image's relative path from the markdown file, return the actual file path
    by resolving the relative path against the markdown file's location or the project root.

    Args:
        image_relative_path (str | Path): The relative path of the image as found in the markdown file.
        markdown_file_path (str | Path): The path to the markdown file.
        root_dir (Path, optional): The root directory of the project, for resolving root-relative paths.

    Returns:
        Path: The resolved absolute path to the image file.
    """
    image_path = Path(image_relative_path)
    markdown_path = Path(markdown_file_path)

    # If the path is absolute, use it directly
    if image_path.is_absolute():
        return image_path

    # If the path starts with '/', it's relative to the project root
    if str(image_path).startswith("/") and root_dir:
        # Remove the leading '/' and join with the root directory
        cleaned_path = str(image_path)[1:] if str(image_path).startswith("/") else str(image_path)
        image_path = root_dir / cleaned_path
        if image_path.exists():
            return image_path.resolve()

    # Try to resolve relative to the markdown file's directory
    image_path_from_md = markdown_path.parent / image_path
    if image_path_from_md.exists():
        return image_path_from_md.resolve()

    # Try to resolve relative to the project root (if provided)
    if root_dir:
        image_path_from_root = root_dir / image_path
        if image_path_from_root.exists():
            return image_path_from_root.resolve()

    # If all resolution attempts fail, return the path relative to the markdown file
    # This might not exist, but it's the best guess
    logger.warning(f"Image path {image_relative_path} could not be resolved to an existing file.")
    return image_path_from_md


def get_unique_id(file_path: str | Path, root_dir: Path) -> str:
    """
    Generate a unique identifier (hash) for the given file path, based on the relative path to the root directory.
    This function normalizes path separators to '/' before hashing to ensure consistency across operating systems.

    Args:
        file_path (str | Path): The file path to hash.
        root_dir (Path): The root directory to which the file path should be relative.

    Returns:
        str: A SHA-256 hash of the normalized relative file path.
    """
    file_path = Path(file_path)
    try:
        # Get the relative path
        rel_path = file_path.relative_to(root_dir)

        # Normalize the path separator to forward slash
        normalized_path = str(rel_path).replace("\\", "/")

        # Generate hash
        hash_obj = hashlib.sha256(normalized_path.encode())
        return hash_obj.hexdigest()[:8]  # First 8 chars of the hash
    except ValueError:
        # If the file is not relative to the root_dir, use the absolute path
        normalized_path = str(file_path.absolute()).replace("\\", "/")
        hash_obj = hashlib.sha256(normalized_path.encode())
        return hash_obj.hexdigest()[:8]  # First 8 chars of the hash


def generate_translated_filename(
    original_filepath: str | Path, language_code: str, root_dir: Path
) -> str:
    """
    Generate a filename for a translated file, including a unique hash and language code.

    Note:
    If the file path and the file name are identical, the same hash will be generated.
    This is because the hash is based on the entire file path.

    Args:
        original_filepath (str): The original file path.
        language_code (str): The language code for the translation (e.g., 'en', 'fr').
        root_dir (Path): The root directory used for generating unique hash IDs.

    Returns:
        str: The translated file's new filename.
    """
    original_filepath = Path(original_filepath)
    filename, extension = get_filename_and_extension(original_filepath)

    # Generate a unique ID based on the file path
    unique_id = get_unique_id(original_filepath, root_dir)

    # Construct the translated filename: original-unique_id-language_code.extension
    return f"{filename}-{unique_id}-{language_code}{extension}"


def get_filename_and_extension(file_path: str | Path) -> tuple[str, str]:
    """
    Extract the filename without extension and the file extension from the given file path.

    Args:
        file_path (str | Path): The file path from which to extract the filename and extension.

    Returns:
        tuple[str, str]: A tuple containing the filename without extension and the file extension.
    """
    file_path = Path(file_path)
    filename = file_path.stem  # Name without extension
    extension = file_path.suffix  # File extension with dot

    # Special handling for multiple extensions like .tar.gz
    if filename.endswith(".tar") and extension == ".gz":
        filename = filename[:-4]  # Remove '.tar'
        extension = ".tar.gz"

    return filename, extension


def filter_files(directory: str | Path, excluded_dirs, extension: str = None) -> list[Path]:
    """
    Filter and return only the files in the given directory, excluding specified directories.
    Optionally filter by file extension.

    Args:
        directory (str | Path): The directory path to search for files.
        excluded_dirs (set): A set of directory names to exclude from the search.
        extension (str, optional): File extension to filter by (e.g., '.ipynb').
                                If None, all file types are included.

    Returns:
        list: A list of Path objects representing only the files (excluding specified directories).
    """
    directory_path = Path(directory)
    result = []

    # Check if the directory exists
    if not directory_path.exists() or not directory_path.is_dir():
        logger.warning(f"Directory does not exist or is not a directory: {directory}")
        return []

    # Walk through the directory
    for root, dirs, files in os.walk(directory_path):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in excluded_dirs]

        # Add files with the specified extension (if extension is provided)
        for file in files:
            file_path = Path(root) / file
            if extension is None or file_path.suffix.lower() == extension.lower():
                result.append(file_path)

    return result


def reset_translation_directories(
    translations_dir: Path, image_dir: Path, language_codes: list
) -> None:
    """
    Remove existing translation and translated_images directories if they exist,
    and then create new ones.

    Args:
        translations_dir (Path): The directory where translations are stored.
        image_dir (Path): The directory where translated images are stored.
        language_codes (list): A list of language codes for creating language-specific directories.
    """
    # Remove existing translation directory if it exists
    if translations_dir.exists():
        shutil.rmtree(translations_dir)

    # Create translation directory
    translations_dir.mkdir(parents=True, exist_ok=True)

    # Create language-specific directories
    for language_code in language_codes:
        lang_dir = translations_dir / language_code
        lang_dir.mkdir(exist_ok=True)

    # Remove existing translated_images directory if it exists
    if image_dir.exists():
        shutil.rmtree(image_dir)

    # Create translated_images directory
    image_dir.mkdir(parents=True, exist_ok=True)


def delete_translated_images_by_language_code(language_code: str, image_dir: Path) -> None:
    """
    Delete all translated images in the given directory that have the specified language code in their filenames.

    Args:
        language_code (str): The language code to filter files by (e.g., 'ko').
        image_dir (Path): The directory where translated images are stored (e.g., './translated_images').
    """
    if not image_dir.exists() or not image_dir.is_dir():
        logger.warning(f"Directory does not exist or is not a directory: {image_dir}")
        return

    # Filter files with the language code in their names
    for file_path in image_dir.glob(f"*-{language_code}.*"):
        if file_path.is_file():
            file_path.unlink()
            logger.debug(f"Deleted translated image: {file_path}")


def delete_translated_markdown_files_by_language_code(
    language_code: str, translations_dir: Path
) -> None:
    """
    Delete the entire directory for the specified language code, including all its contents.

    Args:
        language_code (str): The language code whose folder should be deleted (e.g., 'ko').
        translations_dir (Path): The directory where translated markdown files are stored.
    """
    if not translations_dir.exists() or not translations_dir.is_dir():
        logger.warning(
            f"Directory does not exist or is not a directory: {translations_dir}"
        )
        return

    # Path to the language code directory
    lang_dir = translations_dir / language_code

    # Delete the directory and its contents if it exists
    if lang_dir.exists() and lang_dir.is_dir():
        shutil.rmtree(lang_dir)
        logger.debug(f"Deleted translation directory: {lang_dir}")
    else:
        logger.warning(
            f"Language directory does not exist or is not a directory: {lang_dir}"
        )

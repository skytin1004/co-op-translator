"""
Image translator for handling image-based content translation.
"""
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union
import os
import re

from PIL import Image, ImageDraw, ImageFont
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import io
import tempfile

from ..config.image_config import ImageConfig
from ..llm.text_translator import TextTranslator
from ..utils.vision.image_utils import (
    crop_image, 
    draw_bounding_boxes, 
    extract_image_text,
    get_font_for_language
)

logger = logging.getLogger(__name__)


class ImageTranslator:
    """Translator for image-based content.

    Handles extraction of text from images, translation of that text,
    and generation of new images with the translated text.
    """

    def __init__(self, text_translator: TextTranslator = None):
        """Initialize image translator.

        Args:
            text_translator: Text translator for translating extracted text
        """
        self.vision_client = self._initialize_vision_client()
        self.text_translator = text_translator if text_translator else TextTranslator.create()
        self.config = ImageConfig()

    def _initialize_vision_client(self) -> ComputerVisionClient:
        """Initialize Azure Computer Vision client.

        Returns:
            Configured ComputerVisionClient instance
        """
        try:
            # Get configuration
            image_config = ImageConfig.get_vision_config()
            endpoint = image_config.get("endpoint")
            key = image_config.get("key")
            
            # Create client
            client = ComputerVisionClient(
                endpoint=endpoint,
                credentials=CognitiveServicesCredentials(key)
            )
            
            return client
        except Exception as e:
            logger.error(f"Failed to initialize vision client: {e}")
            return None

    def translate_image(
        self, 
        image_path: Path, 
        target_language: str,
        output_path: Path,
        draw_boxes: bool = False,
        fast_mode: bool = False,
    ) -> bool:
        """
        Translate text in an image to target language.

        Args:
            image_path: Path to the image file
            target_language: Target language code
            output_path: Path to save the translated image
            draw_boxes: Whether to draw bounding boxes around detected text
            fast_mode: Use faster but potentially less accurate translation

        Returns:
            True if translation successful, False otherwise
        """
        try:
            # Extract text from image
            image = Image.open(image_path)
            detected_text = self._extract_text_from_image(image_path)
            
            if not detected_text:
                logger.info(f"No text detected in {image_path}")
                return False
            
            # Translate detected text
            translations = self._translate_detected_text(detected_text, target_language)
            
            # Create translated image
            success = self._create_translated_image(
                image,
                detected_text,
                translations,
                output_path,
                target_language,
                draw_boxes,
                fast_mode
            )
            
            return success
            
        except Exception as e:
            logger.error(f"Error translating image {image_path}: {e}")
            return False

    def _extract_text_from_image(self, image_path: Path) -> List[Dict]:
        """
        Extract text from image using Azure Computer Vision.

        Args:
            image_path: Path to the image file

        Returns:
            List of detected text regions with bounding boxes
        """
        # Implementation would extract text regions from the image
        # For brevity, this is simplified
        try:
            with open(image_path, "rb") as image_file:
                image_data = image_file.read()
                
            # Call Azure Computer Vision API
            results = extract_image_text(self.vision_client, image_data)
            return results
        except Exception as e:
            logger.error(f"Error extracting text from {image_path}: {e}")
            return []

    def _translate_detected_text(
        self, detected_text: List[Dict], target_language: str
    ) -> List[str]:
        """
        Translate detected text regions to target language.

        Args:
            detected_text: List of detected text regions
            target_language: Target language code

        Returns:
            List of translated text strings
        """
        # Extract text lines
        text_lines = [item.get("text", "") for item in detected_text]
        
        # Translate text
        translated_lines = self.text_translator.translate_image_text(text_lines, target_language)
        
        return translated_lines

    def _create_translated_image(
        self,
        original_image: Image.Image,
        detected_text: List[Dict],
        translations: List[str],
        output_path: Path,
        target_language: str,
        draw_boxes: bool = False,
        fast_mode: bool = False,
    ) -> bool:
        """
        Create a new image with translated text.

        Args:
            original_image: Original PIL Image
            detected_text: List of detected text regions
            translations: List of translated text strings
            output_path: Path to save the translated image
            target_language: Target language code
            draw_boxes: Whether to draw bounding boxes around detected text
            fast_mode: Use faster but potentially less accurate translation

        Returns:
            True if successful, False otherwise
        """
        try:
            # Create a copy of the original image
            result_image = original_image.copy()
            draw = ImageDraw.Draw(result_image)
            
            # For each text region and its translation
            for i, (region, translated_text) in enumerate(zip(detected_text, translations)):
                if not translated_text or not region.get("boundingBox"):
                    continue
                    
                # Get bounding box
                box = region.get("boundingBox")
                
                # Get appropriate font for the language
                font = get_font_for_language(target_language, self.config.get_font_size())
                
                # Draw rectangle to cover original text if not in fast mode
                if not fast_mode:
                    draw.rectangle(
                        [box[0], box[1], box[2], box[3]], 
                        fill=(255, 255, 255)
                    )
                
                # Draw translated text
                draw.text(
                    (box[0], box[1]), 
                    translated_text,
                    font=font, 
                    fill=(0, 0, 0)
                )
                
                # Draw bounding box if requested
                if draw_boxes:
                    draw.rectangle(
                        [box[0], box[1], box[2], box[3]], 
                        outline=(255, 0, 0),
                        width=2
                    )
            
            # Create output directory if it doesn't exist
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Save the result
            result_image.save(output_path)
            
            logger.info(f"Translated image saved to {output_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error creating translated image: {e}")
            return False

    @staticmethod
    def create(text_translator: Optional[TextTranslator] = None):
        """Factory method to create an image translator instance.

        Args:
            text_translator: Text translator instance (if None, one will be created)

        Returns:
            ImageTranslator instance
        """
        # Create text translator if not provided
        if text_translator is None:
            text_translator = TextTranslator.create()
            
        return ImageTranslator(text_translator)

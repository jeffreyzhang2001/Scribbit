"""Detects text in the file."""
import os, io
from google.cloud import vision
from google.cloud.vision import types

def ocr(FILE_NAME):
    client = vision.ImageAnnotatorClient()
    with io.open(f'./uploads/{FILE_NAME}', 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    response = client.document_text_detection(image=image)
    #document = response.full_text_annotation.text

    # Returns OCR text with \n formatting
    return(response)
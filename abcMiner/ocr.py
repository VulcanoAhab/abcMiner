import cv2
from PIL import Image
from pytesseract import image_to_string


class Reader:
    """
    Will implement different
    OCR engines
    """
    @classmethod
    def tesseract(cls, grayImage, config=None):
        """
        grayImage: openCV Image Obj
        """
        size=grayImage.shape[:2]
        newSize=tuple([int(s*3) for s in size[::-1]])
        toImage=cv2.resize(grayImage, newSize)
        toTextImage=Image.fromarray(toImage)
        return image_to_string(toTextImage,config=config)

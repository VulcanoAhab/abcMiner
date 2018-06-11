import cv2
from PIL import Image
from pytesseract import image_to_string


class Reader:
    """
    Will implement different
    OCR engines
    """
    @classmethod
    def plainTesseract(cls, grayImage, config=None, sizeScale=0):
        """
        grayImage: openCV Image Obj
        """
        size=grayImage.shape[:2]
        if not sizeScale:
            sizeScale=int(1200/size[-1])
        newSize=tuple([int(s*sizeScale) for s in size[::-1]])
        toImage=cv2.resize(grayImage, newSize)
        toTextImage=Image.fromarray(toImage)
        return image_to_string(toTextImage,config=config)

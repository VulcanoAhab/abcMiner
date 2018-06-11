import cv2
import numpy as np

class File:
    """
    """
    @classmethod
    def openImage(cls, image_path, colorMode):
        """
        """
        img=cv2.imread(image_path)
        return cv2.cvtColor(img, colorMode)

    @classmethod
    def asRgb(cls, image_path):
        """
        """
        return cls.openImage(image_path, cv2.COLOR_BGR2RGB)

    @classmethod
    def asGray(cls, image_path):
        """
        """
        return cls.openImage(image_path, cv2.COLOR_BGR2GRAY)

    @classmethod
    def asHSV(cls, image_path):
        """
        """
        return cls.openImage(image_path, cv2.COLOR_BGR2HSV)

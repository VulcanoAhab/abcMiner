import cv2
import numpy as np
from collections import namedtuple

class Utils:
    """
    """
    _hsvRange=namedtuple("OpenCV_HSV_color_range",["lower","upper"])

    @classmethod
    def hsvRange(cls, lower, upper):
        """
        """
        return cls._hsvRange(np.asarray(lower), np.asarray(upper))


class HSVRanges:
    """
    OpenCV HSV colors ranges
    ------------------------
    H -> 0,180
    S -> 0,255
    V -> 0,255

    Generic colors not build
    for specific detection
    """

    ## not tested
    white=Utils.hsvRange([0, 0,250],[0, 0, 255])
    gray=Utils.hsvRange([0, 0,50],[0, 0, 249])
    yellow=Utils.hsvRange([25, 50,50],[45, 255, 255])
    blue=Utils.hsvRange([90, 50,50],[130, 255, 255])
    blue=Utils.hsvRange([90, 50,50],[130, 255, 255])
    blue=Utils.hsvRange([90, 50,50],[130, 255, 255])
    ## tested
    green=Utils.hsvRange([45, 50,50],[75, 255, 255])
    pink=Utils.hsvRange([150, 200,200],[170, 255, 255])
    orange=Utils.hsvRange([5, 50,50],[15, 250, 250])
    light_red=Utils.hsvRange([0, 255,255],[15, 255, 255])
    intense_red=Utils.hsvRange([171, 250,250],[180, 200, 200])
    purple=Utils.hsvRange([130, 200,50],[155, 255, 255])
    black=Utils.hsvRange([0, 0,0],[0, 0, 50])

    @classmethod
    def hasColor(cls, color):
        """
        """
        return color in cls.__dict__


class Colors:
    """
    """
    @classmethod
    def filterHSV(cls, hsvImage, color):
        """
        image must be HSV color mode
        """
        color_name=color.lower()
        if not HSVRanges.hasColor(color_name):
            raise AttributeError("[-] Unkown color")
        color_range=getattr(HSVRanges, color_name)
        mask=cv2.inRange(hsvImage, color_range.lower, color_range.upper)
        if color_name == "black":
            hsvImage=cv2.bitwise_not(hsvImage)
        return cv2.bitwise_and(hsvImage,hsvImage, mask=mask)

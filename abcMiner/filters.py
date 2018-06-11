import cv2
import numpy as np
from collection import namedtuple

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
    _rangeObj=namedtuple(
        "OpenCV HSV color range",
        ["lower","upper"]
    )
    ## not tested
    white=_rangeObj([0, 0,250],[0, 0, 255])
    gray=_rangeObj([0, 0,50],[0, 0, 249])
    yellow=_rangeObj([25, 50,50],[45, 255, 255])
    blue=_rangeObj([90, 50,50],[130, 255, 255])
    ## tested
    green=_rangeObj([45, 50,50],[75, 255, 255])
    pink=_rangeObj([150, 200,200],[170, 255, 255])
    orange=_rangeObj([5, 50,50],[15, 250, 250])
    light_red=_rangeObj([0, 255,255],[15, 255, 255])
    intense_red=_rangeObj([171, 250,250],[180, 200, 200])
    purple=_rangeObj([130, 200,50],[155, 255, 255])
    black=_rangeObj([0, 0,0],[0, 0, 50])

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
        if not HSVRanges.has(color_name):
            raise AttributeError("[-] Unkown color")
        color_range=getattr(HSVRanges, color_name)
        mask=cv2.inRange(hsvImage,color_range.lower, color_range.upper)
        if color_name == "black":
            hsvImage=cv2.bitwise_not(hsvImage)
        return cv2.bitwise_and(hsvImage,hsvImage, mask=mask)

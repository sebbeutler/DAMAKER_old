
from enum import Enum
from typing import NamedTuple, Optional


class FilePathStr(str):
    pass
class FolderPathStr(str):
    pass

class NamedArray:
    name: str=""
    data: list=[]

class PixelSize(NamedTuple):
    Z: Optional[float]
    Y: Optional[float]
    X: Optional[float]

    def __str__(self):
        return f'X: {self.X:.2f} Y: {self.Y:.2f} Z: {self.Z:.2f}'

class MesureUnit(Enum):
    none: str = 'Ø'
    micro: str = 'µm'

    def strToUnit(text):
        if text == 'µm':
            return MesureUnit.micro
        return MesureUnit.none

class Size():
    width: int
    height: int

class Point():
    x: int
    y: int
class PointF():
    x: float
    y: float

class Line():
    p1: Point
    p2: Point
class LineF():
    p1: Point
    p2: Point

class Rect():
    pos: Point
    size: Size
class RectF():
    pos: Point
    size: Size

class Circle():
    center: Point
    radius: int
class CircleF():
    center: Point
    radius: float

import inspect


def method(func):

    def method_decorator(self, *args, **kwargs):
        ret = func(self, *args, **kwargs)
        if inspect.signature(func).return_annotation is inspect._empty:
            ret = self
        return ret

    return method_decorator

import inspect
from dataclasses import dataclass
from enum import Enum
from functools import wraps
from typing import Any, NamedTuple, Optional, Callable

# TODOC

# DECORATORS #

def method(func):
    def method_decorator(self, *args, **kwargs):
        ret = func(self, *args, **kwargs)
        if inspect.signature(func).return_annotation is inspect._empty:
            ret = self
        return ret

    return method_decorator

def obselete(msg: str='', avi=True):
    def obselete_wrapper(func):
        def obselete_decorator(*args, **kwargs):
            if not avi:
                raise ObseleteCallException()
            print(f'[WARNING]: Usage of an obselete function {func.__name__}.')
            return func(*args, **kwargs)
        return obselete_decorator
    return obselete_wrapper

# TYPES #

class FilePathStr(str):
    pass
class FolderPathStr(str):
    pass
class DmkUnkown():
    pass
DamakerPluginLoader = Callable[[str], Any]

# TUPLES / ENUMS #

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

# GEOMETRY #

@dataclass
class Size():
    width: int
    height: int

@dataclass
class Point():
    x: int
    y: int

@dataclass
class PointF():
    x: float
    y: float

@dataclass
class Line():
    p1: Point
    p2: Point

@dataclass
class LineF():
    p1: Point
    p2: Point

@dataclass
class Rect():
    pos: Point
    size: Size

@dataclass
class RectF():
    pos: Point
    size: Size

@dataclass
class Circle():
    center: Point
    radius: int

@dataclass
class CircleF():
    center: Point
    radius: float

# EXCEPTIONS #

class DamakerException(Exception):
    pass

class FormatMismatchException(DamakerException):
    pass

class DimensionCountMismatchException(DamakerException):
    pass

class LengthMismatchException(DamakerException):
    pass

class ShapeMismatchException(DamakerException):
    pass

class OperationMissingOutputException(DamakerException):
    pass

class ObseleteCallException(DamakerException):
    pass
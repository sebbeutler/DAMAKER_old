import os
from typing import Any, Callable, Tuple

import numpy as np
from typing_extensions import Self

from .dmktypes import *

@dataclass
class ImageStackMetadata:
    pixelsize: PixelSize = None
    unit: MesureUnit = None
    filepath: FilePathStr = None
    lut: np.ndarray = None

    @property
    def basename(self) -> str:
        if self.filepath != None:
            return os.path.basename(self.filepath)
        else: return 'Unamed'

    def __str__(self) -> str:
        return \
f'''
pixelsize: {self.pixelsize}
unit: {self.unit.value}
filepath: {self.filepath}
'''

    def __iter__(self) -> iter:
        return iter(self.__dict__.items())

@dataclass
class ImageStack:
    data: np.ndarray = None
    metadata: ImageStackMetadata = None

    data_loader: Callable[[str], np.ndarray] = None
    metadata_loader: Callable[[str], ImageStackMetadata] = None

    @property
    def shape(self) -> Tuple[int, ...]:
        if issubclass(type(self.data), np.ndarray):
            return self.data.shape
        return ()

    @property
    def format(self) -> type:
        if issubclass(type(self.data), np.ndarray):
            return self.data.dtype
        return ()

    @property
    def ndim(self) -> int:
        if issubclass(type(self.data), np.ndarray):
            return len(self.data.shape)
        return 0

    @method
    def setDataLoader(self, loader):
        self.data_loader = loader

    @method
    def setMetadataLoader(self, loader):
        self.metadata_loader = loader

    @method
    def loadAll(self, filepath: FilePathStr):
# TODO: missing , end='' in the print ( it was causing error in logging for GUI)
        if self.data_loader != None:
            print("loading data : ")
            self.data = self.data_loader(filepath)

        if self.metadata_loader != None:
            print("loading metadata : ")
            self.metadata = self.metadata_loader(filepath)

        print('')

        if self.metadata != None:
            self.metadata.filepath = filepath

    @method
    def clone(self, data=None, metadata=None) -> Self:
        cloned = ImageStack()

        cloned.metadata_loader = self.metadata_loader
        cloned.data_loader = self.data_loader

        cloned.metadata =  metadata if metadata != None else self.metadata
        cloned.data =  data if type(data) is np.ndarray else self.data.copy()

        return cloned

    @method
    def get(self, metadata_id: str) -> Any:
        return self.metadata.__dict__[metadata_id]  if self.metadata != None else None

    @method
    def set(self, metadata_id: str, value):
        if self.metadata == None:
            self.metadata = ImageStackMetadata()
        self.metadata.__dict__[metadata_id] = value

    def __str__(self) -> str:
        return f'shape: {self.shape}\n' + \
            f'format: {self.format}\n' + \
            str(self.metadata)

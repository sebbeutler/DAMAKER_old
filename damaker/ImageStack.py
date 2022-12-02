from typing import Tuple

import numpy as np

from .dmktypes import *


class ImageStackMetadata:
    pixelsize: PixelSize
    unit: MesureUnit
    filepath: FilePathStr

    def __str__(self):
        return f'''\
pixelsize: {self.pixelsize}
unit: {self.unit.value}
filepath: {self.filepath}
'''

class ImageStack:
    data: np.ndarray
    metadata: ImageStackMetadata

    data_loader=None
    metadata_loader=None

    @method
    def shape(self) -> Tuple[int, ...]:
        if issubclass(type(self.data), np.ndarray):
            return self.data.shape
        return ()

    @method
    def format(self) -> type:
        if issubclass(type(self.data), np.ndarray):
            return self.data.dtype
        return ()

    @method
    def setDataLoader(self, loader):
        self.data_loader = loader

    @method
    def setMetadataLoader(self, loader):
        self.metadata_loader = loader

    @method
    def loadAll(self, filepath: FilePathStr):

        print("loading data : ", end='')
        self.data = self.data_loader(filepath)

        print("loading metadata : ", end='')
        self.metadata = self.metadata_loader(filepath)
        print('')

        if self.metadata != None:
            self.metadata.filepath = filepath

    def __str__(self):
        return f'shape: {self.shape()}\n' + \
            f'format: {self.format()}\n' + \
            str(self.metadata)

import enum
import os
import sys
from inspect import signature, Signature
from typing import Callable
from collections.abc import Iterable

# DMK_DIR = os.path.dirname(sys.argv[0])
DMK_DIR = os.getcwd()
PLUGINS_DIR = f'{DMK_DIR}/plugins/'

def _createPluginsFolder():
    if not os.path.exists(PLUGINS_DIR):
        os.mkdir(PLUGINS_DIR)
        with open(f'{PLUGINS_DIR}/__init__.py', 'w') as initFile:
            initFile.write("""
# To import a file 'plugins/myFile.py'
# from .myFile import *

# Or put the functions directly here

# # -Example 1- #
# def myFunc(param1: str, param2: int) -> bool:
# 	print("do something.")
# 	return True

# # -Example 2- #
# from damaker.Channel import Channel
# def myOperation(input: Channel) -> Channel:
# 	# process channel here.
# 	return input
""")

from .dmktypes import *
from .ImageStack import *

def importPlugins():
    _createPluginsFolder()
    import importlib.util
    spec = importlib.util.spec_from_file_location("plugins", f'{PLUGINS_DIR}/__init__.py')
    foo = importlib.util.module_from_spec(spec)
    sys.modules["plugins"] = foo
    spec.loader.exec_module(foo)
    import plugins
    return plugins

class Operation():
    alias: str
    category: str
    func: Callable
    signature: Signature
    hits: dict

    def __init__(self, alias: str, category: str, func: Callable, _signature: Signature, hints: dict):
        self.alias = alias
        self.category = category
        self.func = func
        self.signature = _signature
        self.hints = hints

__operations__: dict[str, Operation] = {}

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

# Operation DECORATOR #
def operation(**hints):
    global __operations__
    def damaker_operation_decorator(func: Callable):
        alias: str = hints.get('alias')
        category: str = hints.get('category')
        ndim_hint = hints.get('ndim')

        if alias == None:
            alias = func.__name__
        if category == None:
            category = 'Plugins'

        __operations__[alias] = Operation(alias, category, func, signature(func), hints)

        def damaker_operation_wrapper(*args, **kwargs):
            print(f'>> Running {alias}')
            if ndim_hint != None:
                if issubclass(type(args[0]), ImageStack):
                    input: ImageStack = args[0]
                    if (isinstance(ndim_hint, Iterable) and input.ndim not in ndim_hint) or input.ndim != ndim_hint:
                        raise DimensionCountMismatchException()
            return func(*args, **kwargs)
        return damaker_operation_wrapper
    return damaker_operation_decorator

# TODO MAAAAAAAAAIN PIPELINEEEE, should be ez bro, then you need to do the modalities
# actually maybe just put the baseline for the pipeline, then you make sure all the GUI is
# is working properly then u can chill
# from .pipeline import *
from .processing import *
from .utils import *


class BuiltInDataLoader(enum.Enum):
    TIFFILE = utils._dataloader_tiffile
    AICSI = utils._dataloader_aicsi
    BIOFORMATS = utils._dataloader_bioformats

class BuiltInMetadataLoader(enum.Enum):
    BIOFORMATS = utils._metadataloader_bioformats

def load(filepath: FilePathStr, data_loader=BuiltInDataLoader.TIFFILE, metadata_loader=BuiltInMetadataLoader.BIOFORMATS) -> ImageStack:
    """
        Name: Import file
        Category: Import
    """
    # biofile = bioformats_reader.BioFile(filepath)
    # metadata = biofile.ome_metadata
    # px_sizes = PhysicalPixelSize(
    #     metadata.images[0].pixels.physical_size_z,
    #     metadata.images[0].pixels.physical_size_y,
    #     metadata.images[0].pixels.physical_size_x
    # )

    if not os.path.isfile(filepath):
        print("Cannot load '" + filepath + "', file not found.")
        return None

    stack = ImageStack()

    return stack                            \
        .setDataLoader(data_loader)         \
        .setMetadataLoader(metadata_loader) \
        .loadAll(filepath)
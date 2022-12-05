import enum
import os
import sys

import damaker.dmktypes as dmktypes
import damaker.utils as utils

from .imagestack import ImageStack, ImageStackMetadata
from .operation import Operation, OperationInput
from .pipeline import Pipeline


DMK_DIR = os.getcwd()
PLUGINS_DIR = f'{DMK_DIR}/plugins/'

def _createPluginsFolder():
    if not os.path.exists(PLUGINS_DIR):
        os.mkdir(PLUGINS_DIR)
        with open(f'{PLUGINS_DIR}/__init__.py', 'w') as initFile:
            initFile.write(\
"""

import damaker

# # -Example 1- #
#
# @damaker.Operation(alias='MaFonction', category='Export')
# def myFunc(param1: str, param2: int) -> bool:
# 	print("do something.")
# 	return True

# # -Example 2- #
# @damaker.Operation(ndim=3)
# def myOperation(input: ImageStack) -> ImageStack:
# 	# process channel here.
# 	return input

""")

from types import ModuleType

def importPlugins() -> ModuleType:
    _createPluginsFolder()
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "plugins",
        f'{PLUGINS_DIR}/__init__.py'
    )
    foo = importlib.util.module_from_spec(spec)
    sys.modules["plugins"] = foo
    spec.loader.exec_module(foo)
    import plugins
    return plugins

class DataLoaderBuiltIn(enum.Enum):
    TIFFILE = utils._dataloader_tiffile
    AICSI = utils._dataloader_aicsi
    BIOFORMATS = utils._dataloader_bioformats

class MetadataLoaderBuiltIn(enum.Enum):
    BIOFORMATS = utils._metadataloader_bioformats

def load(
    filepath: dmktypes.FilePathStr,
    data_loader=DataLoaderBuiltIn.TIFFILE,
    metadata_loader=MetadataLoaderBuiltIn.BIOFORMATS
) -> ImageStack:
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

def close():
    utils.javabridge.kill_vm()
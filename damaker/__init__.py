import os
import sys

import damaker.dmktypes as dmktypes
import damaker.stream as stream

from .imagestack import ImageStack, ImageStackMetadata
from .operation import Operation, OperationInput
from .pipeline import Pipeline
from .stream import load


DMK_DIR = os.getcwd()
PLUGINS_DIR = f'{DMK_DIR}/plugins/'

# TODO: replace by importlib.reload
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

def close():
    stream.javabridge.kill_vm()


def _createPluginsFolder():
    if not os.path.exists(PLUGINS_DIR):
        os.mkdir(PLUGINS_DIR)
        with open(f'{PLUGINS_DIR}/__init__.py', 'w') as initFile:
            initFile.write(\
"""

import damaker


# # -Example 1- #

# @damaker.Operation(alias='MaFonction', category='Export')
# def myFunc(param1: str, param2: int) -> bool:
# 	print("do something.")
# 	return True


# # -Example 2- #

# @damaker.Operation(ndim=3)
# def myOperation(input: ImageStack) -> ImageStack:
# 	# process channel here.
# 	return input


# # -Example .tif loader- #

# @damaker.data_loader(alias='My Loader', files=['.tif', '.tiff'])
# def myLoader(filepath: str) -> np.ndarray: 
#     with TiffFile(filename) as file:
#         data = file.asarray()
#     return data

""")

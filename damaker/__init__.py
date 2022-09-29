import sys, os

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

def importPlugins():
    _createPluginsFolder()
    import importlib.util
    spec = importlib.util.spec_from_file_location("plugins", f'{PLUGINS_DIR}/__init__.py')
    foo = importlib.util.module_from_spec(spec)
    sys.modules["plugins"] = foo
    spec.loader.exec_module(foo)
    import plugins
    return plugins

from .Channel import *
from .pipeline import *
from .processing import *
from .utils import *

def load(*args):
    return loadChannelsFromFile(*args)
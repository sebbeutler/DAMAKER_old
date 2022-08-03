import sys, os

# DMK_DIR = os.path.dirname(sys.argv[0])
DMK_DIR = os.getcwd()
PLUGINS_DIR = f'{DMK_DIR}/plugins/'
if not os.path.exists(PLUGINS_DIR):
    os.mkdir(PLUGINS_DIR)
    open(f'{PLUGINS_DIR}/__init__.py', 'w').close()

def importPlugins():
    import importlib.util
    spec = importlib.util.spec_from_file_location("plugins", f'{PLUGINS_DIR}/__init__.py')
    foo = importlib.util.module_from_spec(spec)
    sys.modules["plugins"] = foo
    spec.loader.exec_module(foo)
    import plugins
    return plugins

importPlugins()

import plugins
from plugins import *

from .Channel import *
from .pipeline import *
from .processing import *
from .utils import *
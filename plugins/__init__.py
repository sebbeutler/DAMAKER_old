import os, sys

CURRENT_PATH = os.path.dirname(__file__)

def _loadRScript(filename):
    import rpy2.robjects as robjects
    r = robjects.r

    r.source(f'{CURRENT_PATH}/{filename}')

    # Updating function list #
    for key, val in robjects.globalenv.items():
        if isinstance(val, robjects.functions.Function):
            setattr(sys.modules[__name__], key, val)
            # plugins.f1.rcall(keyvals=(("nb.int", 5),))

# Python files #
from .ExamplePlugin import *

# R files #
_loadRScript('ExamplePlugin.R')
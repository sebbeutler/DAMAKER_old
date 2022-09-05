
# Python files #
from .ExamplePlugin import *


# R files #

import os, sys
import rpy2.robjects as robjects

r = robjects.r
data = r.source(f'{os.path.dirname(__file__)}/ExamplePlugin.R')

for var in data:
    if isinstance(var, robjects.functions.Function):
        setattr(sys.modules[__name__], "f1", var)
        # plugins.f1.rcall(keyvals=(("nb.int", 5),))
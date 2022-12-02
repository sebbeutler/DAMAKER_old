# %%
import os
# os.environ['JAVA_HOME'] = 'C:/Program Files/Java/jdk-11.0.13'
# os.environ["JAVA_HOME"] = "C:/Users/PC/anaconda3/envs/dmk/Library" 

import damaker, javabridge
from importlib import reload

stack = damaker.load('resources/E1.tif')
print(stack)
javabridge.kill_vm()

# %%

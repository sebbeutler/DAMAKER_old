# %%
import os
# os.environ['JAVA_HOME'] = 'C:/Program Files/Java/jdk-11.0.13'
# os.environ["JAVA_HOME"] = "C:/Users/PC/anaconda3/envs/dmk/Library" 

import javabridge
import damaker_gui
damaker_gui.run(exit=False)
javabridge.kill_vm()

#%%
# from aicsimageio import AICSImage

# img = AICSImage('resources/E1.tif')  # selects the first scene found
# a = img.data  # returns 5D TCZYX numpy array
# b = img.xarray_data
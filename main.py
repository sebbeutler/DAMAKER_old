# %%
import os
# os.environ['JAVA_HOME'] = 'C:/Program Files/Java/jdk-11.0.13'
# os.environ["JAVA_HOME"] = "C:/Users/PC/anaconda3/envs/dmk/Library" 

# import damaker as dmk
#from importlib import reload

import damaker
img = damaker.load('resources/E1.tif')
img.data = img.data[0]
print(img)
img_inv = damaker.processing.channelReverse(img)
print(img_inv)
print(damaker.__operations__['Reverse stack'].hints)


# %%

# %%
import os
# os.environ['JAVA_HOME'] = 'C:/Program Files/Java/jdk-11.0.13'
# os.environ["JAVA_HOME"] = "C:/Users/PC/anaconda3/envs/dmk/Library" 

import javabridge
import damaker_gui
damaker_gui.run(exit=False)
javabridge.kill_vm()



#%%

# import damaker as dmk
# metadata = dmk.utils._loadMetadata_bioformats('/home/sdv/m1isdd/sbeutler/Bureau/DAMAKER/resources/E1.tif')
# chns = dmk.loadChannelsFromFile('/home/sdv/m1isdd/sbeutler/Bureau/DAMAKER/resources/E1.tif')
# dmk.utils.channelSave(chns[0], "./")

# %%
# import javabridge
# import bioformats as bio

# javabridge.start_vm(class_path=bio.JARS)

# data = bio.get_omexml_metadata("/home/sdv/m1isdd/sbeutler/Bureau/DAMAKER/resources/E1.tif")

# import xmltodict

# dict_ome = xmltodict.parse(data)
# dict_ome['OME']['Image']

# %%

# from damaker import plugins
# print(plugins.myOperation.__annotations__)

# try:
#     from damaker import plugins
#     plugins.f2()
# except Exception: print("No plugins")



# import damaker
# from damaker_gui.widgets.PreviewWidget import getLut
# import pyqtgraph as pg
# import numpy as np
# import tiffile
# import zarr
# from aicsimageio.writers import OmeTiffWriter
# from ome_types.model import OME
# lut = getLut("red")   

# chn = damaker.loadChannelsFromFile("E1.ome.tif")
# # print(chn[0].metadata)
# print(chn[0].shape)

# tiffile.imwrite('EE.tif', np.array([chn[0].data, chn[1].data]), (2,) + chn[0].shape, np.uint8)
# with tiffile.TiffWriter('EE.tif') as file:
#     file.write(np.array([chn[0].data, chn[1].data]))
    

# tiffile.TiffWriter()
# OmeTiffWriter.save(chn.data, "test2", physical_pixel_sizes=chn.px_sizes, dim_order="ZYX", channel_colors=lut.getStops(1)[1][:, :3])
# print(chn.metadata)
# OmeTiffWriter.save(chn.data, "test2", physical_pixel_sizes=chn.px_sizes, dim_order="ZYX", ome_xml=chn.metadata)


# print(len(lut.getStops(pg.ColorMap.BYTE)[1]))
import damaker_gui
damaker_gui.run()

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
from utils import *
from processing import *
from vedo import *
from pipeline import *

from py4j.java_gateway import JavaGateway
from py4j.java_collections import JavaArray



# gateway = JavaGateway()


# arr = np.zeros((200, 200), dtype=np.uint8)

# chn = loadChannel("../resources/segmentation/C1-E0.tif")[0]

# arr = bytes(chn.data.flatten().tolist())
# z, y, x = chn.shape

# img = gateway.entry_point.numpyToImagePlus(arr, x, y, z)
# gateway.entry_point.runSegmentation(img, "../../resources/segmentation/CU1.model", "../../resources/segmentation/out.tif")
# chn = loadChannel("../resources/segmentation/C1-E0.tif")[0]
# plotChannel(chn)

# gateway.entry_point.runSegmentation("../../resources/segmentation/C1-E0.tif", "../../resources/segmentation/CU1.model", "../../resources/segmentation/out.tif")
# gateway.shutdown()

# chn = loadChannel("../resources/segmentation/out.tif")[0]
# channelFromBinary(chn)
# channelInvert(chn)
# plotChannel(chn)

m1 = Mesh("result/average_th4.obj")
m2 = Mesh("result/average_th5.obj")

vol = Volume(dims=(400, 400, 100), spacing=(0.5,0.5,1.2), origin=(-1,-1,-1))

volpts = vol.topoints().alpha(0.2)
volpts.distanceTo(merge(m1,m2)).print()

# assign these values to the volume
arr = volpts.pointdata["Distance"] * 100
vol.pointdata["Distance"] = arr.astype(np.uint8)

# vol.show()
# save to disk as tiff stack
# vol.write('test.tif')

# make a Volume slice (as Mesh) and add coloring to make it visible
xslc = vol.xSlice(10).cmap("flag")

show(m1, m2, volpts, xslc, axes=1).close()
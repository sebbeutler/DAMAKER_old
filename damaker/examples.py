# import damaker


# # -Example 1- #

# @damaker.Operation(alias='MaFonction', category='Export')
# def myFunc(param1: str, param2: int) -> bool:
# 	print("do something.")
# 	return True


# # -Example 2- #

# @damaker.Operation(ndim=3)
# def myOperation(input: ImageStack) -> ImageStack:
# 	# process channel here.
# 	return input


# # -Example .tif loader- #

# @damaker.data_loader(alias='My Loader', files=['.tif', '.tiff'])
# def myLoader(filepath: str) -> np.ndarray: 
#     with TiffFile(filename) as file:
#         data = file.asarray()
#     return data
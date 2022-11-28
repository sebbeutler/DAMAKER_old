from setuptools import setup

##############################################################
setup(
    name="damaker",
    python_requires=">=3.8",
    version="0.0.1",
    packages=[
               "damaker",
               "damaker_gui",
    ],

    package_dir={
                  'damaker': 'damaker',
                  'damaker_gui': 'damaker_gui',
    },

    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "imageio",
        "aicsimageio",
        "tifffile",
        "bioformats-jar",
        # "python-bioformats",
        # "python-javabridge",
        # "rpy2",
        "py4j",
        "PySide2",
        "PyOpenGL",
        "pyqtgraph",
        "opencv-python",
        "Pillow",
        "scikit-image",
        "SimpleITK",
        "vedo",
        "vtk",
        "xmlschema",
        "xmltodict",
        ],
    include_package_data=True,
)
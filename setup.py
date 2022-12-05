from setuptools import setup

# python setup.py build && python -m build
# twine upload --repository testpypi dist/*
# pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ damaker

##############################################################
setup(
    name = "damaker",
    python_requires = ">=3.8",
    version = "0.3.0",
    packages = [
        "damaker",
        "damaker_gui",
    ],

    package_dir = {
        'damaker': 'damaker',
        'damaker_gui': 'damaker_gui',
    },

    install_requires = [
        'numpy',
        'pandas',
        'scipy',
        'matplotlib',
        'imageio',
        'aicsimageio',
        'tifffile',
        'bioformats-jar',
        'python-bioformats',
        'python-javabridge',
        # 'rpy2',
        'py4j',
        'PySide2',
        'PyOpenGL',
        'pyqtgraph',
        'opencv-python',
        'Pillow',
        'scikit-image',
        'scikit-learn',
        'SimpleITK',
        'vedo',
        'vtk',
        'xmlschema',
        'xmltodict',
        ],
    include_package_data = True,
)
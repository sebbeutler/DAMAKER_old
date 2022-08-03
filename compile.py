import os

# TODO: exclude unused module. see: https://stackoverflow.com/questions/4890159/python-excluding-modules-pyinstaller

# -Settings-
_EXENAME = 'v0.2.7-alpha.DAMAKER'
_STANDALONE = False
_ICON  = f'{os.path.dirname(__file__)}/damaker_gui/resources/icons/16x16/damaker.ico'
_COMPRESS = False

# -Build commande-
cmd = f"""pyinstaller
main.py
    -y
    -n {_EXENAME}{'.standalone' if _STANDALONE else '.full'}
    {'--onefile' if _STANDALONE else '' }
    --windowed
    
    --icon={_ICON}
    {'--upx-dir=dist/upx-3.96-win64' if _COMPRESS else ' '}
    
    --collect-all "xmlschema"
    --collect-all "vedo"
    --collect-all "py4j"
    --collect-all "pyqtgraph"
    --collect-all "ome_types"
    
    --hidden-import "vtkmodules"
    --hidden-import "vtkmodules.all"
    --hidden-import "vtkmodules.util.numpy_support"
"""

# -Execution- #
if __name__ == '__main__':
    print('exec: ', cmd)
    os.system(cmd.replace('\n', ' '))
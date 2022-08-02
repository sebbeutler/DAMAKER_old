# DAMAKER

## Build with conda
```
conda create -n damaker python=3.9 -y
conda activate damaker
conda install -c conda-forge scyjava -y
pip install -r Requirements.txt```

`python main.py`

`pyinstaller -n Damaker -w --collect-all "xmlschema" --collect-all "vtkmodules" --collect-all "vedo" --collect-all "py4j"  --collect-all "pyqtgraph" --collect-all "ome_types" main.py -y`

`pyinstaller -n Damaker -w -F --collect-all "xmlschema"  --collect-all "vedo" --collect-all "py4j"  --collect-all "pyqtgraph" --collect-all "ome_types" --hidden-import "vtkmodules" --hidden-import "vtkmodules.all" --hidden-import "vtkmodules.util.numpy_support" main.py -y`

`pyinstaller -n Damaker --onefile --windowed --icon=damaker_gui/resources/icons/16x16/damaker.ico --upx-dir=dist/upx-3.96-win64 --collect-all "xmlschema"  --collect-all "vedo" --collect-all "py4j"  --collect-all "pyqtgraph" --collect-all "ome_types" --hidden-import "vtkmodules" --hidden-import "vtkmodules.all" --hidden-import "vtkmodules.util.numpy_support" main.py -y`

### Related links

- github : https://github.com/subski/DAMAKER
- trello : https://trello.com/b/bgtG1JQn/conduite-de-projet
- macros : https://github.com/cristinapujades/Blanc-et-al.-2022
- DAMAKER paper : https://www.biorxiv.org/content/10.1101/2021.03.29.437592v2

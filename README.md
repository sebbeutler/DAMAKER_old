# DAMAKER

- binaries: https://github.com/subski/DAMAKER/releases
- pip: https://test.pypi.org/project/damaker/0.3.0/
- documentation: damaker.readthedocs.io/en/latest/
- github: https://github.com/subski/DAMAKER
- trello : https://trello.com/b/bgtG1JQn/damaker

## Install (pip)

```bash
# From test.pypi.org
python -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ damaker
```

## Build with conda

```bash
conda create -n damaker python=3.10 -y
conda activate damaker
# conda install -c conda-forge m2w64-gcc scyjava openjdk -y # Recommended

git clone https://github.com/subski/DAMAKER.git

pip install -r Requirements.txt
```

## Run Graphical Interface

```bash
python main.py
```

```python
import damaker_gui
damaker_gui.run()
```

## Build binaries

```bash
python compile.py
```

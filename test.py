import numpy as np

import pyqtgraph as pg

win = pg.GraphicsLayoutWidget(show=True)
win.resize(800,350)
plt1 = win.addPlot()

vals = np.hstack([np.random.normal(size=500), np.random.normal(size=260, loc=4)])

y,x = np.histogram(vals, bins=np.linspace(-3, 8, 40))

plt1.plot(x, y, stepMode="center", fillLevel=0, fillOutline=True, brush=(0,0,255,150))

if __name__ == '__main__':
    pg.exec()

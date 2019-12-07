import numpy as np
import intDir
import plotter

n = 100
h = 1 / n

X = np.arange(0, 1+h, h)
Y = np.arange(0, 1+h, h)

I = np.array(intDir.integr(len(X)))

plotter.plotSurface(X, Y, I)
plotter.plotContour(X, Y, I, 1000)
plotter.plotPcolor(X, Y, I)
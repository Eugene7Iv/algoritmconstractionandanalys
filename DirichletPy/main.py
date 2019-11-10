import numpy as np
import dirichlet
import intdif
import plotter

n = 100
h = 1 / n

#U = np.array(dirichlet.solDirichlet(n_= n, iterCount_ = 100, writeToFile = True))
G = np.array(dirichlet.getDirichlet(n, 20, h))

#plotter.plotSurface(np.array(U), h = h)
plotter.plotSurface(np.array(G), h = h)


#plotter.plotContour(U, h = h)
#plotter.plotContour(G, h = h)
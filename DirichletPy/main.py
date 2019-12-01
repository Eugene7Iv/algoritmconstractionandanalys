import numpy as np
import dirichlet
import intdif
import plotter

def writeToFile(U, sfile):
    n = len(U)

    for i in range(0, n):
        for j in range(0 , n):
            sfile.write('%4f' % U[i][j] + '\t')
        sfile.write('\n')

n = 100
h = 1 / n

X = np.arange(0, 1+h, h)
Y = np.arange(0, 1+h, h)

U = np.array(dirichlet.solDirichlet(len(X)))
G = np.array(dirichlet.getDirichlet(X, Y))

plotter.plotSurface(X, Y, U)
plotter.plotContour(X, Y, U)

plotter.plotSurface(X, Y, G)
plotter.plotContour(X, Y, G)
import numpy as np
import dirichlet
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

print('error = ', dirichlet.error(U,G))

plotter.plotSurface(X, Y, U, 'Numerical Solution')
plotter.plotSurface(X, Y, G, 'Analitical Sulution')
plotter.plotContour(X, Y, U, 'Numerical Solution')
plotter.plotContour(X, Y, G, 'Analitical Sulution')
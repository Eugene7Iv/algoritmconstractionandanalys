from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
import numpy as np
from matplotlib import cm


def plotSurface(X, Y, U, title = ""):
    fig = plt.figure('Surface ' + title)
    ax = fig.gca(projection='3d')

    # Make data.
    xlen = len(X)
    ylen = len(Y)
    zMax = np.amax(U)
    zMin = np.amin(U)

    X, Y = np.meshgrid(X, Y)
    # Plot the surface
    surf = ax.plot_surface(X, Y, U,cmap=cm.coolwarm)

    # Customize the z axis.
    ax.set_zlim(zMin, zMax)
    ax.w_zaxis.set_major_locator(LinearLocator(6))

    plt.show()

def plotContour(X, Y, U, title = ""):
    xlen = len(X)
    ylen = len(Y)

    fig = plt.figure('Contour ' + title)
    
    X, Y = np.meshgrid(X, Y)
    cset = plt.contour(X, Y, U, cmap=cm.coolwarm)

    plt.show()

def foo(X, Y, U):
    plt.pcolor(X, Y, U, cmap=cm.coolwarm)
    plt.colorbar()
    plt.show()
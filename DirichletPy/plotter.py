from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
import numpy as np
from matplotlib import cm


def plotSurface(X, Y, U):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Make data.
    xlen = len(X)
    ylen = len(Y)
    zMax = np.amax(U)
    zMin = np.amin(U)

    X, Y = np.meshgrid(X, Y)
    # Plot the surface
    surf = ax.plot_surface(X, Y, U)

    # Customize the z axis.
    ax.set_zlim(zMin, zMax)
    ax.w_zaxis.set_major_locator(LinearLocator(6))

    plt.show()

def plotContour(X, Y, U):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    xlen = len(X)
    ylen = len(Y)
    X, Y = np.meshgrid(X, Y)
    cset = ax.contour(X, Y, U, cmap=cm.coolwarm)
    ax.clabel(cset, fontsize=9, inline=1)

    plt.show()

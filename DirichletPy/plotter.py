from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
import numpy as np
from matplotlib import cm


def plotSurface(U_, h = 0.1):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Make data.
    X = np.arange(0, 1, h)
    xlen = len(X)
    Y = np.arange(0, 1, h)
    ylen = len(Y)
    X, Y = np.meshgrid(X, Y)
    U = np.array(U_)

    # Plot the surface
    surf = ax.plot_surface(X, Y, U)

    # Customize the z axis.
    ax.set_zlim(0, 1)
    ax.w_zaxis.set_major_locator(LinearLocator(6))

    plt.show()

def plotContour(U_, h = 0.1):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X = np.arange(0, 1, h)
    xlen = len(X)
    Y = np.arange(0, 1, h)
    ylen = len(Y)
    X, Y = np.meshgrid(X, Y)
    U = np.array(U_)
    cset = ax.contour(X, Y, U, cmap=cm.coolwarm)
    ax.clabel(cset, fontsize=9, inline=1)

    plt.show()

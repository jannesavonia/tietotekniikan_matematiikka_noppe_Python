import numpy as np 
from matplotlib import pyplot as plt 
import matplotlib.patches as mpatches

def vect3d_plot(x, y, z, x_label, y_label, z_label):
    ax = plt.figure().add_subplot(projection='3d')
    ax.set_aspect('equal')
    ax.axes.set_xlim3d(left=-0.5, right=1.5) 
    ax.axes.set_ylim3d(bottom=-0.5, top=1.5) 
    ax.axes.set_zlim3d(bottom=0, top=2) 
    ax.xaxis.set_ticklabels([])
    ax.yaxis.set_ticklabels([])
    ax.zaxis.set_ticklabels([])
    ax.set_xlabel(r'$x_1$')
    ax.set_ylabel(r'$x_2$')
    ax.set_zlabel(r'$x_3$')

    #Draw projections 1st
    x_proj=np.append(x[:2], [0])
    y_proj=np.append(y[:2], [0])
    z_proj=np.append(z[:2], [0])
    ax.quiver(0, 0, 0, *x_proj, color='gray')
    ax.quiver(0, 0, 0, *y_proj, color='gray')
    ax.quiver(0, 0, 0, *z_proj, color='gray')

    #Draw vectors
    ax.quiver(0, 0, 0, *x, color='r')
    ax.quiver(0, 0, 0, *y, color='b')
    ax.quiver(0, 0, 0, *z, color='m')

    #Add legend
    x_patch = mpatches.Patch(color='r', label=x_label)
    y_patch = mpatches.Patch(color='b', label=y_label)
    z_patch = mpatches.Patch(color='m', label=z_label)
    plt.legend(handles=[x_patch, y_patch, z_patch], 
        loc='upper left', framealpha=0.5, frameon=True)

    return ax
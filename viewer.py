from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np

def tri_plot(x,y,topo):
    """
    This is a super simple function to plot a triangular mesh.
    It is also an interesting exercize to see how to loop over the
    mesh elementzs. ``x`` and ``y`` are one dimensional arrays containg the nodes
    coordinates. On each row of the ``topo`` matrix is stored the
    dof (degree of freedom) with support on the row-th element. Notice that
    we are looping over the first dimension of ``topo``, so we only need to
    write a standard ``python`` for loop:

    .. code:: python

        for row in topo:

    The ``numpy`` command ``hstack`` is used to attach the last node to the
    first one. This is done to "close" our triangles.

    .. code:: python

       row = np.hstack([row,row[0]])

    We use the ``[`` ``]`` brackets to acces the nodes and define the local coords.

    .. code:: python

       x_l = x[row]
       y_l = y[row]

    Now we only need to plot the local coords for every triangle:

    .. code:: python

       plt.plot(x_l, y_l,'-b',linewidth=2)

    """
    for row in topo:
        row = np.hstack([row,row[0]])
        x_l = x[row]
        y_l = y[row]
        plt.plot(x_l, y_l,'-b',linewidth=2)

    plt.show()

    return


def plot_sol_p1(x,y,z,topo):

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.plot_trisurf(x, y, z, cmap=cm.jet,vmin=min(z), vmax=max(z), linewidth=0.2)

    plt.show()
    return

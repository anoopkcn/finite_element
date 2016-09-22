from basis_func import *
import numpy as np

def gradu_gradv(topo,x,y):
    """ A assembly code """
    return A

def f_v(topo,x,y):
    """ F assembly code
    Input :

    topo : Information about the topology of the triangles. \n
    x    : An (n,3) array of n evaluation points with columns x1, x2, x3. \n
    y    : An (n,3) array of n evaluation points with columns y1, y2, y3. \n

    Output :

    F    : The RHS of poisson's equation

    Notice :
    """
    for element in topo:
        x_l = x[element]
        y_l = y[element]
        (dx_phi,dy_phi,phi,surf_e) = tri_p1(x_l,y_l,np.zeros((1,2)))

        F=surf_e/3.*np.ones((x.shape[0]))

    return F

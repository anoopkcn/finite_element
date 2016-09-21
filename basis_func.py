import numpy as np

def tri_p1(x,y,eval_p):
    """
    Linear shape function on triangles, namely p1.

    Input:

    x : one dimensional array of triangle vertices x coords.\n
    y : one dimensional array of triangle vertices y coords.\n
    eval_p: (n,2) array of the n evaluation points. first
            column indicates x-coord, second y-coord.\n

    Output:

    dx_phi : the three x-derivatives.\n
    dy_phi : the three y-derivatives.\n
    phi    : (n,3) array of the three shape funtions ath the n eval points.\n
    surf_e : the triangle area.\n

    Notice: all the quantities are computed on the current element

    """
    return dx_phi,dy_phi,phi[0],surf_e

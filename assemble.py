from basis_func import *
import numpy as np

def gradu_gradv(topo,x,y):
    """
    
    OUTPUT:
    the matrix which will be used in the LHS of the final linear system
    """
    global_matrix = np.zeros((x.shape[0],x.shape[0])) 
    # square matrix, as many rows and cols as there are nodes
    for element in topo:
        
        # let K denote the current element (a triangle, here)
        # x_local, y_local store the coords of the vertices of K
        x_K = x[element]
        y_K = y[element]
        
        # dx_phi, dy_phi are x,y derivatives of the phi_i of K,
        # phi stores the value of each phi_i evaluated at (quadrature) points in K
        # surf_local is the area of K
        (dx_phi, dy_phi, phi, surf_K) = tri_p1(x_K, y_K, np.zeros((1,2)) )
        
        # every K contributes to global_matrix with a 3x3 matrix called K_matrix
        K_matrix = np.zeros((3,3))        
        for i in range(0,3):
            for j in range(0,3):
                K_matrix[i,j] = surf_K *\
                (dx_phi[i]*dx_phi[j] + dy_phi[i]*dy_phi[j])
        
        # add K_matrix to global_matrix
        for i in range(0,3):
            for j in range(0,3):
                A[element[i], element[j]] += K_matrix[i,j]
    
    return global_matrix

def f_v(topo,x,y):
    """ F assembly code """
    return F

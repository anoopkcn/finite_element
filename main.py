import numpy as np

from mesh import *
from basis_func import *
from assemble import *

from viewer import *

def clear_rows(A,b_nodes):
    """ code to clear rows with nodes lying on the boundary
    Input :

    A      : The (n,n) matrix (where n is the number of nodes) which has in the LHS of the final linear system.
    b_nodes: The list specifying the boundary nodes

    Output :

    A : The matrix after applying the boundary conditions

    """
    n=np.len(A)
    for i in (0,n):
        for j in (0,n):
            for k in b_nodes:
                if (i==k and i!=j):
                    A[i][j]=0

    return A

    # sould be cleard when running main.py
    A_clear = clear_rows(A,b_nodes)
    sol = np.linalg.solve(np.asmatrix(A_clear),np.asmatrix(F))



if __name__ == "__main__":

    topo , x , y , nodes , b_nodes = read_msh("mesh/square.msh")
    A = gradu_gradv(topo,x,y)
    F = f_v(topo,x,y)
    F[b_nodes]=0
    A_clear = clear_rows(A,b_nodes)
    sol = np.linalg.solve(np.asmatrix(A_clear),np.asmatrix(F))
    plot_sol_p1(x,y,sol,topo)

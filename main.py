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
    n=len(A)
    for i in b_nodes:
        A[i][i+1:]=0
        A[i][:i]=0
    return A


if __name__ == "__main__":

    # replace "square" by "HQSquare", "l_sh", "half_circle" for other shapes
    topo , x , y , nodes , b_nodes = read_msh("mesh/square.msh")
    A = gradu_gradv(topo,x,y)
    F = f_v(topo,x,y)
    F[b_nodes]=0
    A_clear = clear_rows(A,b_nodes)
    sol = np.linalg.solve(A_clear,F)
    plot_sol_p1(x,y,sol,topo)

	#Uncomment what follows to plot the difference between the difference between the
	#approximation of actual solution, and the output of "finite elements"
    
	#actual_sol = np.sin(np.pi * x) * np.sin(np.pi * y)
    #diff = sol - actual_sol
    #plot_sol_p1(x,y,diff,topo)


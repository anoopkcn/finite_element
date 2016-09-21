import numpy as np

#INPUT: a file, containing vertices and (0-, 1-, and 2-dimensional) elements
#       appropriately tagged (see square.msh)

#OUTPUT: 

def read_msh(filename):
    
    x = np.array([])
    y = np.array([])
    
    topo = np.empty([0,3], dtype=int)
    
    nodes = np.array([], dtype=int)
    b_nodes = np.array([], dtype=int)

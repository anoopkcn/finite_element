import numpy as np

"""
Input :
the name of a file containing mesh points (nodes)
    and elements (boundary segments, triangles)

Output : 
(E is the number of elements, N is the number of nodes)
topo: an (E,3) array containing for each element the labels of its vertices
    e.g. if "i" has vertices 1, 4, 142 in the mesh file, topo[i] = [0,3,141]
nodes: an array of length N. nodes[i] = i-1
b_nodes: an array containing the boundary nodes in an unspecified order.
    b_nodes[i] can be zero (0 =< b_nodes[i] =< N - 1)
x, y: two arrays (of length N). 
    x[nodes[i]],y[nodes[i]] are the cartesian coords of the vertex i
    (i.e. x[i-1], y[i-1] are the coords of the vertex i)
"""
def read_msh(filename):
    
    # initialize all
    x = np.array([])
    y = np.array([])
    
    topo = np.empty([0,3], dtype=int)

    amount_nodes = 0
    nodes = np.array([], dtype=int)
    b_nodes = np.array([],dtype=int)
        
    # open file    
    f = open(filename,'r')

    for line in f:
        l = line.split()
        if line[0] == '$': # skip this line
            continue 
        elif len(l) == 4: # it's a node
            amount_nodes += 1 
            l = map(float, l)
            x = np.append(x, l[2])
            y = np.append(y, l[3])
        elif len(l) == 7: # it's a boundary segment
            l = map(int, l)
            extremities = l[5:]
            for i in extremities:
                if i-1 not in b_nodes:
                    b_nodes = np.append(b_nodes,i-1)    
        elif len(l) == 8: # it's a 2-dimensional element (a triangle)
            l = map(int, l)
            topo_row = np.array(l[5:]) - 1
            topo = np.vstack((topo, topo_row))
    
    nodes = np.arange(amount_nodes - 1)

    f.close()

    #now reverse the orientation, if needed
    r_id = 0
    for row in topo:
        ck =      (x[row[1]]-x[row[0]])*(y[row[2]]-y[row[0]])
        ck = ck - (x[row[2]]-x[row[0]])*(y[row[1]]-y[row[0]])
        if ck < 0:
            topo[r_id,:] = np.array([[row[0],row[2],row[1]]])
        r_id+=1

    return topo , x , y , nodes , b_nodes

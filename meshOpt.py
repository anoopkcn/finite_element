import numpy as np

#INPUT: a file, containing vertices and (0-, 1-, and 2-dimensional) elements
#       appropriately tagged (see square.msh)

#OUTPUT: 

def read_msh(filename):
    
    x = np.array([])
    y = np.array([])
    
    topo = np.empty([0,3], dtype=int)
    
    nodes_amount = 0
    nodes = np.array([], dtype=int)
    b_nodes = np.array([], dtype=int)

    f = open(filename, 'r')

    # in the Input, these strings mark beginning/end of reading nodes/elements
    begin_nodes = '$Nodes'
    end_nodes = '$EndNodes'
    begin_elements = '$Elements'
    end_elements = '$EndElements'

    # in the Input, the second entry of an element has a tag marking
    # whether it is a boundary segment, or a triangle, or other
    boundary_segment = '1'
    triangle = '2'

    # get the amount of nodes 
    is_reading_nodes = False
    for line in f:
        if is_reading_nodes:
            nodes_amount = int(line) # store the amount of nodes
            break 
        elif line != begin_nodes:
            continue 
        elif line == begin_nodes:
            is_reading_nodes = True # next line contains the amount of nodes
            continue

    nodes = np.arange(nodes_amount - 1)
    
    # I hope it goes on with the line at which it broke!
    # get the coords of the nodes
    for line in f:
        if line == end_nodes: # check that there are still nodes to read
            is_reading_nodes = False
            break
        l = line.split()
        x = np.append(x, l[2])
        y = np.append(y, l[3])

    is_reading_elements = False
    for line in f:
        if is_reading_element: # if so, read them
            l = line.split()
            if str(l[1]) == boundary_segment: # it's a border 1-dim element
                l = map(int, l)
                extremities = l[-2:] # last 2 elems are its vertices
                for i in extremities:
                    if i-1 not in b_nodes: 
                        b_nodes = np.append(b_nodes,i-1)
            elif str(l[1]) == triangle: # it's a 2-dim element
                l = map(int, l)
                topo_row = np.array(l[-3:]) # last 3 elems are its vertices
                topo = np.vstack((topo, topo_row))
            elif line == end_elements: # we are done, break
                is_reading_elements = False
                break
            else: # it's not a border node or a 2-dim element, skip "line"
                continue           
        elif line == begin_elements: # we are about read elements
            is_reading_elements = True
        elif line != begin_elements: # skip "line" wait for '$Elements'
            continue

    topo = topo - 1

return topo, x, y, nodes, b_nodes

        

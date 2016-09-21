import numpy as np

#output should be topo, x, y, b_nodes
#TODO: nodes is not really updated (nor tested)
#      

def read_msh(filename):

    x = np.array([])
    y = np.array([])
    
    topo = np.empty([0,3], dtype=int)

    nodes = np.array([], dtype=int)
    b_nodes = np.array([],dtype=int)
        

    

    f = open(filename,'r')

    for line in f:
        l = line.split()
        if line[0] == '$':
            print "this is useless"
        elif len(l) == 4:
            l = map(float, l)
            x = np.append(x, l[2])
            y = np.append(y, l[3])
        elif len(l) == 7:
            l = map(int, l)
            extremities = l[5:]
            for i in extremities:
                if i-1 not in b_nodes: #does this really exist? IT DOES
                    b_nodes = np.append(b_nodes,i-1)    
        elif len(l) == 8:
            l = map(int, l)
            topo_row = np.array(l[5:])
            topo = np.vstack((topo, topo_row))
            #print topo_row
            #print type(topo)
    
    #numbering is off by one
    topo = topo - 1
    print topo #comment me out

    f.close()

    #now reverse the orientation, if needed
    r_id = 0
    for row in topo:
        ck =      (x[row[1]]-x[row[0]])*(y[row[2]]-y[row[0]])
        ck = ck - (x[row[2]]-x[row[0]])*(y[row[1]]-y[row[0]])
        if ck < 0:
            topo[r_id,:] = np.array([[row[0],row[2],row[1]]])
        r_id+=1

    print r_id
    return topo , x , y , nodes , b_nodes

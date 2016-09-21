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
    n=len(eval_p)
    a=np.zeros(3);b=np.zeros(3);c=np.zeros(3),np.zeros(n)
    M=np.array([[x[0],y[0],1],[x[1],y[1],1],[x[2],y[2],1]])
    eig_val=np.array([[1,0,0],[0,1,0],[0,0,1]])

    for i in range(0,3):
        a[i],b[i],c[i]=np.linalg.solve(np.asmatrix(M),eig_val[i])


    for i in  range(0,n):
        for j in range(0,3):
            phi[j]=a[j]*eval_p[i][0]+b[j]*eval_p[i][1]+c[j]

    return 0
    # return dx_phi,dy_phi,phi[0],surf_e

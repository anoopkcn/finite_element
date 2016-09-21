import numpy as np
import basis_func as bf

x = np.array([0.,1.,0.])
y = np.array([0.,0.,1.])
print bf.tri_p1(x,y,np.array([.1,.2]))

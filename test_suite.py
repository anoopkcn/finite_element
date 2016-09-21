from __future__ import division
import unittest
from mesh import *
from basis_func import *
from assemble import *
import numpy as np

def almost_equal(a, b, digits):
    if (abs(a)<10**-10 and abs(b)<10**-10):
        return True
    epsilon = 10 ** -digits
    return abs(a/b - 1) < epsilon

def lists_almost_equal(a,b,digits):
    for i,j in zip(a,b):
        truth = almost_equal(i, j, digits)
        if truth == False:
            return truth
    return truth

def matrix_almost_equal(a,b,digits):
    print 'a = ', a
    print 'b = ', b
    for i,j in zip(a,b):
        truth = lists_almost_equal(i, j, digits)
        if truth == False:
            return truth
    return truth

class BasisFuncsTest(unittest.TestCase):
    def test_basis_func_00(self):
        x = np.array([0.,1.,0.])
        y = np.array([0.,0.,1.])
        dx_phi,dy_phi,phi,surf_e = tri_p1(x,y,np.array([.1,.2]))
        self.assertTrue(almost_equal(surf_e,.5,1))
        self.assertTrue(lists_almost_equal(dx_phi, [-1., 1., 0.],1))
        self.assertTrue(lists_almost_equal(dy_phi, [-1., 0., 1.],1))
        self.assertTrue(lists_almost_equal(phi,[0.7, 0.1, 0.2],1))
    def test_basis_func_01(self):
        x = np.array([1.,1.,0.])
        y = np.array([0.,1.,1.])
        dx_phi,dy_phi,phi,surf_e = tri_p1(x,y,np.array([.9,.8]))
        self.assertTrue(almost_equal(surf_e,.5,1))
        self.assertTrue(lists_almost_equal(dx_phi, [0.,1.,-1.],1))
        self.assertTrue(lists_almost_equal(dy_phi, [-1.,1.,0.],1))
        self.assertTrue(lists_almost_equal(phi,[0.2 ,0.7, 0.1],1))


class MeshTest(unittest.TestCase):
    def test_read_msh(self):
        expected = np.array([ 65,129,85],dtype=np.int_)
        topo , x , y , nodes , b_nodes = read_msh('mesh/square.msh')
        result = topo[10,:]
        self.assertItemsEqual(result, expected)
        self.assertItemsEqual(b_nodes[:5], [0,4,5,6,7])
        # assertCountEqual for python 3

class AssembleTest(unittest.TestCase):
    def test_assemble(self):
        #topo , x , y , nodes , b_nodes = read_msh('mesh/square.msh')
        topo = np.array([[0,1,2]])
        x = np.array([0.,1.,0.])
        y = np.array([0.,0.,1.])
        expected = np.array([[ 1.,-.5,-.5],[-.5,.5,0.],[-.5,0.,.5]])
        lm = gradu_gradv(topo , x , y)
        truth = matrix_almost_equal(lm,expected,3)
        self.assertTrue(truth)
        f = f_v(topo,x,y)
        expected = np.array([ 0.16666667,0.16666667,0.16666667])
        truth = lists_almost_equal(f,expected,5)
        self.assertTrue(truth)
        #self.assertItemsEqual(result, expected)
        #self.assertItemsEqual(b_nodes[:5], [0,4,5,6,7])

if __name__ == "__main__":
    unittest.main()

#FINITE ELEMENTS
##Introduction
The finite element method (FEM) is a numerical technique for finding approximate solutions to boundary value problems for partial differential equations. In other words it can be used to find solutions to problems that can be expressed into 'governing equations' and 'boundary conditions'.


![theory](images/fem.png?raw=true)


One of the relatively easy problems to sole with FEM is the **Poisson's problem, modeling the diffusion of temperature in a body**. Which we are trying to solve using this code.

##Basic Algorithm
The `main.py` file takes an (n,n) matrix (where n is the number of nodes) which has in the LHS of the final linear system. With the help of a vector `b_nodes` which specifying the boundary nodes it gives the matrix after applying the boundary conditions.

The file `get_param` recives the mesh type given in the `parametes.txt`file and the force that is specified in the same file.

The file `basis_func.py` takes `x`, a  one dimensional array of triangle vertices x coordinates, and `y`, a one dimensional array of triangle vertices y coords. `eval_p` an (n,2) array of the n evaluation points: the first column stores x-coords, the second y-coords. It returns as output `phi`, an (n,3) array of the three shape funtions at the n eval points, `dx_phi`, the three x-derivatives, ` dy_phi`, the three y-derivatives, and `surf_e` the triangle area.


##Parameters
The parameters one can use are described in the file _parameters.txt_

###Available options
Change the rhs of the above equalities to change the parameters.
The available parameters are:

- force: the function of the right hand side of the heat equation
- mesh: the triangulation of the domain on which the equation will be solved

Currently, the available options for each parameter are:

- force:
    - sinsin: (2pi^2)sin(pix)sin(piy)
    - one: 1 (the constant function 1)

- mesh:
    - square: a square of side 1, ms=0.1 (286 elements)
    - HQsquare: a square of side 1, ms=0.02 (6874 elements)
    - l\_sh: an L-shape (three squares, each of side 1, for the L-shape)
    - half\_circle: a half circle

##Results

**Result 1 : Numerical solution** (force = sinsin, mesh = HQsquare)
![theory](images/solution_with_forcing.png?raw=true)


**Result 2 : Difference with the theoretical value and the numerical solution** (force = sinsin, mesh = HQsquare)
![theory](images/difference_from_actual_solution.png?raw=true)

**Result 3: Numerical solution** (force = sinsin, mesh = half\_circle)
![theory](images/force_sinsin_mesh_half_circle.png?raw=true)

As one can see from the above plot the program is accurate up to the fourth decimal place.



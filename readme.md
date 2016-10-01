#FINITE ELEMENTS
##Introduction
The finite element method (FEM) is a numerical technique for finding approximate solutions to boundary value problems for partial differential equations. In other words it can be used to find solutions to problems that can be expressed into 'governing equations' and 'boundary conditions'.


![theory](images/fem.png?raw=true)


One of the relatively easy problems to sole with FEM is the **Poisson's problem, modeling the diffusion of temperature in a body**. Which we are trying to solve using this code.

##Basic Algorithm
-The `main.py` file takes an (n,n) matrix (where n is the number of nodes) which has in the LHS of the final linear system. With the help of a vector(`b_nodes` which specifying the boundary nodes it gives the matrix after applying the boundary conditions.

- The parameters one can use are(given in the file _parametes.txt_

PARAMETERS

force = one

mesh = square

AVAILABLE OPTIONS 

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

WARNING 

The name of this file has to be `parameters.txt`.

This file has to be in the same folder as `assemble.py` and `main.py`.

The format of the "parameters lines" has to be: <parameter\_name> = <option\_name>

The file `get_param` recives the mesh type given in the `parametes.txt`file and the force that is specified in the same file.

File `basis_func.py` takes `x` a  one dimensional array of triangle vertices x coords. `y` a one dimensional array of triangle vertices y coords. `eval_p` an (n,2) array of the n evaluation points. first column indicates x-coord, second y-coord. Gives the output `dx_phi` the three x-derivatives. ` dy_phi` the three y-derivatives.`phi` an (n,3) array of the three shape funtions ath the n eval points.`surf_e` the triangle area.


##Results

**Result 1 : Numerical solution**
![theory](images/solution_with_forcing.png?raw=true)


**Result 2 : Difference with the theoretical value and the numerical solution**
![theory](images/difference_from_actual_solution.png?raw=true)


**As one can see from the above plot the program is accurate up to the 4<sup>th</sup> decimal place.**



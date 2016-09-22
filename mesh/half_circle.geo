// Gmsh project created on Wed Sep 21 20:57:39 2016
ms = 0.1;
Point(1) = {0, 0, 0, ms};
Point(2) = {1, 0, 0, ms};
Point(3) = {-1, 0, 0, ms};
Point(4) = {0, 1, 0, ms};

Circle(1) = {2, 1, 4};
Circle(2) = {4, 1, 3};
Line(3) = {3, 1};
Line(4) = {1, 2};
Line Loop(5) = {2, 3, 4, 1};
Plane Surface(6) = {5};

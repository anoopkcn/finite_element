// Gmsh project created on Thu Sep 22 19:12:52 2016
ms=0.1;
Point(1) = {0, 0, 0, ms};
Point(2) = {1, 0, 0, ms};
Point(3) = {1,.5, 0, ms};
Point(4) = {.5, .5, 0, ms};
Point(5) = {.5, 1, 0, ms};
Point(6) = {0, 1, 0, ms};
Line(1) = {6, 1};
Line(2) = {2, 1};
Line(3) = {3, 2};
Line(4) = {4, 3};
Line(5) = {5, 4};
Line(6) = {6, 5};
Line Loop(7) = {4, 3, 2, -1, 6, 5};
Plane Surface(8) = {7};
Plane Surface(9) = {7};

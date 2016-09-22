// Gmsh project created on Wed Sep 21 20:26:40 2016
ms = .1;
Point(1) = {0, 0, 0, ms};
Point(2) = {1, 0, 0, ms};
Point(3) = {1,.5, 0, ms};
Point(4) = {.5,.5,0, ms};
Point(5) = {.5,1, 0, ms};
Point(6) = {0, 1, 0, ms};
Line(1) = {6, 5};
Line(2) = {5, 4};
Line(3) = {4, 3};
Line(4) = {3, 2};
Line(5) = {2, 1};
Line(6) = {1, 6};
Line Loop(7) = {1, 2, 3, 4, 5, 6};
Plane Surface(8) = {7};

You are given four points ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A,B,C) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;D) in a 3-dimensional Cartesian coordinate system. You are required to print the angle between the plane made by the points ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A,B,C) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B,C,D) in degrees(__not radians__). Let the angle be ![equation](http://latex.codecogs.com/svg.latex?\inline&space;PHI). 

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20Cos%28PHI%29%20%3D%20%28X.Y%29/%7CX%7C%7CY%7C) where  ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20X%20%3D%20AB)x![equation](http://latex.codecogs.com/svg.latex?\inline&space;BC)  and  ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20Y%20%3D%20BC)x ![equation](http://latex.codecogs.com/svg.latex?\inline&space;CD).

Here, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;X.Y) means the dot product of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;X) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;Y), and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;AB) x ![equation](http://latex.codecogs.com/svg.latex?\inline&space;BC) means the cross product of vectors ![equation](http://latex.codecogs.com/svg.latex?\inline&space;AB) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;BC). Also, ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20AB%20%3D%20B%20-%20A).

__Input Format__

One line of input containing the space separated floating number values of the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;X,Y) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;Z) coordinates of a point.

__Output Format__

Output the angle correct up to two decimal places.

__Sample Input__
```commandline
0 4 5
1 7 6
0 5 9
1 7 2
```
__Sample Output__
```commandline
8.19
```
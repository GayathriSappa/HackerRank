[Polar coordinates](https://en.wikipedia.org/wiki/Polar_coordinate_system) are an alternative way of representing Cartesian coordinates or [Complex Numbers](https://en.wikipedia.org/wiki/Complex_number).

A complex number ![equation](http://latex.codecogs.com/svg.latex?\inline&space;z) 

![](https://github.com/avtomato/HackerRank/blob/master/Python/img/OUzGu.png)

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20z%20%3D%20x%20&plus;%20yj)

is completely determined by its real part ![equation](http://latex.codecogs.com/svg.latex?\inline&space;x) and imaginary part ![equation](http://latex.codecogs.com/svg.latex?\inline&space;y).<br> 
Here, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;j) is the [imaginary unit](https://en.wikipedia.org/wiki/Imaginary_unit).

A polar coordinate (![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20r%2C%5Cvarphi)) 

![](https://github.com/avtomato/HackerRank/blob/master/Python/img/1440141121-5b051fd241-Capture.PNG)

is completely determined by modulus ![equation](http://latex.codecogs.com/svg.latex?\inline&space;r) and phase angle ![equation](http://latex.codecogs.com/svg.latex?\inline&space;\varphi).

If we convert complex number ![equation](http://latex.codecogs.com/svg.latex?\inline&space;z) to its polar coordinate, we find:<br>
![equation](http://latex.codecogs.com/svg.latex?\inline&space;r): Distance from ![equation](http://latex.codecogs.com/svg.latex?\inline&space;z) to origin, i.e.![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20%5Csqrt%7Bx%5E2%20&plus;%20y%5E2%7D),<br> 
![equation](http://latex.codecogs.com/svg.latex?\inline&space;\varphi): Counter clockwise angle measured from the positive ![equation](http://latex.codecogs.com/svg.latex?\inline&space;x)-axis to the line segment that joins ![equation](http://latex.codecogs.com/svg.latex?\inline&space;z) to the origin.

Python's [cmath](https://docs.python.org/2/library/cmath.html) module provides access to the mathematical functions for complex numbers.

![equation](http://latex.codecogs.com/svg.latex?\inline&space;cmath.phase)<br> 
This tool returns the phase of complex number ![equation](http://latex.codecogs.com/svg.latex?\inline&space;z) (also known as the argument of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;z)).
```python
>>> phase(complex(-1.0, 0.0))
3.1415926535897931
``` 
![equation](http://latex.codecogs.com/svg.latex?\inline&space;abs)<br>
This tool returns the modulus (absolute value) of complex number ![equation](http://latex.codecogs.com/svg.latex?\inline&space;z).
```python
>>> abs(complex(-1.0, 0.0))
1.0
```
__Task__
 
You are given a complex ![equation](http://latex.codecogs.com/svg.latex?\inline&space;z). Your task is to convert it to polar coordinates.

__Input Format__

A single line containing the complex number ![equation](http://latex.codecogs.com/svg.latex?\inline&space;z). Note: complex() function can be used in python to convert the input as a complex number.

__Constraints__

Given number is a valid complex number

__Output Format__

Output two lines:<br> 
The first line should contain the value of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;r).<br> 
The second line should contain the value of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;\varphi).

__Sample Input__
```commandline
  1+2j
```
__Sample Output__
```commandline
 2.23606797749979 
 1.1071487177940904
```
__Note: The output should be correct up to 3 decimal places.__

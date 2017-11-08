[dot](http://docs.scipy.org/doc/numpy/reference/generated/numpy.dot.html)

The dot tool returns the dot product of two arrays.
```python
import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.dot(A, B)       #Output : 11
```
[cross](http://docs.scipy.org/doc/numpy/reference/generated/numpy.cross.html)

The cross tool returns the cross product of two arrays.
```python
import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.cross(A, B)     #Output : -2
```
__Task__

You are given two arrays ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B). Both have dimensions of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N)X![equation](http://latex.codecogs.com/svg.latex?\inline&space;N). <br>
Your task is to compute their [matrix product](https://en.wikipedia.org/wiki/Matrix_multiplication#Matrix_product_.28two_matrices.29).

__Input Format__

The first line contains the integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N). <br>
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) space separated integers of array ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A). <br>
The following ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) space separated integers of array ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B).

__Output Format__

Print the matrix multiplication of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B).

__Sample Input__
```commandline
2
1 2
3 4
1 2
3 4
```
__Sample Output__
```commandline
[[ 7 10]
 [15 22]]
```
[identity](http://docs.scipy.org/doc/numpy/reference/generated/numpy.identity.html#numpy.identity)

The identity tool returns an identity array. An identity array is a square matrix with all the main diagonal elements as ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1) and the rest as ![equation](http://latex.codecogs.com/svg.latex?\inline&space;0). The default type of elements is float.
```python
import numpy
print numpy.identity(3) #3 is for  dimension 3 X 3

#Output
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
```
[eye](http://docs.scipy.org/doc/numpy/reference/generated/numpy.eye.html#numpy-eye)

The eye tool returns a 2-D array with ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1)'s as the diagonal and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;0)'s elsewhere. The diagonal can be main, upper or lower depending on the optional parameter ![equation](http://latex.codecogs.com/svg.latex?\inline&space;k). A positive ![equation](http://latex.codecogs.com/svg.latex?\inline&space;k) is for the upper diagonal, a negative ![equation](http://latex.codecogs.com/svg.latex?\inline&space;k) is for the lower, and a ![equation](http://latex.codecogs.com/svg.latex?\inline&space;0) ![equation](http://latex.codecogs.com/svg.latex?\inline&space;k) (default) is for the main diagonal.
```python
import numpy
print numpy.eye(8, 7, k = 1)    # 8 X 7 Dimensional array with first upper diagonal 1.

#Output
[[ 0.  1.  0.  0.  0.  0.  0.]
 [ 0.  0.  1.  0.  0.  0.  0.]
 [ 0.  0.  0.  1.  0.  0.  0.]
 [ 0.  0.  0.  0.  1.  0.  0.]
 [ 0.  0.  0.  0.  0.  1.  0.]
 [ 0.  0.  0.  0.  0.  0.  1.]
 [ 0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.]]

print numpy.eye(8, 7, k = -2)   # 8 X 7 Dimensional array with second lower diagonal 1.
```

__Task__

Your task is to print an array of size ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N)X![equation](http://latex.codecogs.com/svg.latex?\inline&space;M) with its main diagonal elements as ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1)'s and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;0)'s everywhere else.

__Input Format__

A single line containing the space separated values of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M). <br>
![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) denotes the rows. <br>
![equation](http://latex.codecogs.com/svg.latex?\inline&space;M) denotes the columns.

__Output Format__

Print the desired ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N)X![equation](http://latex.codecogs.com/svg.latex?\inline&space;M) array.

__Sample Input__
```commandline
3 3
```
__Sample Output__
```commandline
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
```
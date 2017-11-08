The NumPy module also comes with a number of built-in routines for linear algebra calculations. These can be found in the sub-module linalg.

[linalg.det](http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.det.html)

The linalg.det tool computes the determinant of an array.
```python
print numpy.linalg.det([[1 , 2], [2, 1]])       #Output : -3.0
```
[linalg.eig](http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.eig.html)

The linalg.eig computes the eigenvalues and right eigenvectors of a square array.
```python
vals, vecs = numpy.linalg.eig([[1 , 2], [2, 1]])
print vals                                      #Output : [ 3. -1.]
print vecs                                      #Output : [[ 0.70710678 -0.70710678]
                                                #          [ 0.70710678  0.70710678]]
```
[linalg.inv](http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.inv.html)

The linalg.inv tool computes the (multiplicative) inverse of a matrix.
```python
print numpy.linalg.inv([[1 , 2], [2, 1]])       #Output : [[-0.33333333  0.66666667]
                                                #          [ 0.66666667 -0.33333333]]
```
Other routines can be found [here](http://docs.scipy.org/doc/numpy/reference/routines.linalg.html)

__Task__

You are given a square matrix ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) with dimensions ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N)X![equation](http://latex.codecogs.com/svg.latex?\inline&space;N). Your task is to find the determinant.

__Input Format__

The first line contains the integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N). <br>
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines contains the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) space separated elements of array ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A).

__Output Format__

Print the determinant of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A).

__Sample Input__
```commandline
2
1.1 1.1
1.1 1.1
```
__Sample Output__
```commandline
0.0
```
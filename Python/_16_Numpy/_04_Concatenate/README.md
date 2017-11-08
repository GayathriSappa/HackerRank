[Concatenate](http://docs.scipy.org/doc/numpy/reference/generated/numpy.concatenate.html)

Two or more arrays can be concatenated together using the concatenate function with a tuple of the arrays to be joined:
```python
import numpy

array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])

print numpy.concatenate((array_1, array_2, array_3))    

#Output
[1 2 3 4 5 6 7 8 9]
```
If an array has more than one dimension, it is possible to specify the axis along which multiple arrays are concatenated. By default, it is along the first dimension.
```python
import numpy

array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])

print numpy.concatenate((array_1, array_2), axis = 1)   

#Output
[[1 2 3 0 0 0]
 [0 0 0 7 8 9]] 
```   
__Task__

You are given two integer arrays of size ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N)X![equation](http://latex.codecogs.com/svg.latex?\inline&space;P) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M)X![equation](http://latex.codecogs.com/svg.latex?\inline&space;P) (![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) & ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M) are rows, and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;P) is the column). Your task is to concatenate the arrays along axis ![equation](http://latex.codecogs.com/svg.latex?\inline&space;0).

__Input Format__

The first line contains space separated integers ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;P). <br> 
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines contains the space separated elements of the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;P) columns. <br>
After that, the next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M) lines contains the space separated elements of the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;P) columns.

__Output Format__

Print the concatenated array of size ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20%28N%20&plus;%20M%29)X![equation](http://latex.codecogs.com/svg.latex?\inline&space;P).

__Sample Input__
```commandline
4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4
``` 
__Sample Output__
```commandline
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 
```
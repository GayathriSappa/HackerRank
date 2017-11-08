[Transpose](http://docs.scipy.org/doc/numpy/reference/generated/numpy.transpose.html#numpy-transpose)

We can generate the transposition of an array using the tool numpy.transpose. <br>
It will not affect the original array, but it will create a new array.
```python
import numpy

my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print numpy.transpose(my_array)

#Output
[[1 4]
 [2 5]
 [3 6]]
```
[Flatten](http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.flatten.html)

The tool flatten creates a copy of the input array flattened to one dimension.
```python
import numpy

my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print my_array.flatten()

#Output
[1 2 3 4 5 6]
```
__Task__

You are given a ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N)X![equation](http://latex.codecogs.com/svg.latex?\inline&space;M) integer array matrix with space separated elements (![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) = rows and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M) = columns). <br>
Your task is to print the transpose and flatten results.

__Input Format__

The first line contains the space separated values of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M). <br>
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines contains the space separated elements of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M) columns.

__Output Format__

First, print the transpose array and then print the flatten.

__Sample Input__
```commandline
2 2
1 2
3 4
```
__Sample Output__
```commandline
[[1 3]
 [2 4]]
[1 2 3 4]
```
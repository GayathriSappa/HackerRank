[mean](http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html)

The mean tool computes the arithmetic mean along the specified axis.
```python
import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.mean(my_array, axis = 0)        #Output : [ 2.  3.]
print numpy.mean(my_array, axis = 1)        #Output : [ 1.5  3.5]
print numpy.mean(my_array, axis = None)     #Output : 2.5
print numpy.mean(my_array)                  #Output : 2.5
```
By default, the axis is None. Therefore, it computes the mean of the flattened array.

[var](http://docs.scipy.org/doc/numpy/reference/generated/numpy.var.html#numpy-var)

The var tool computes the arithmetic variance along the specified axis.
```python
import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.var(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.var(my_array, axis = 1)         #Output : [ 0.25  0.25]
print numpy.var(my_array, axis = None)      #Output : 1.25
print numpy.var(my_array)                   #Output : 1.25
```
By default, the axis is None. Therefore, it computes the variance of the flattened array.

[std](http://docs.scipy.org/doc/numpy/reference/generated/numpy.std.html#numpy.std)

The std tool computes the arithmetic standard deviation along the specified axis.
```python
import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.std(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.std(my_array, axis = 1)         #Output : [ 0.5  0.5]
print numpy.std(my_array, axis = None)      #Output : 1.11803398875
print numpy.std(my_array)                   #Output : 1.11803398875
```
By default, the axis is None. Therefore, it computes the standard deviation of the flattened array.

__Task__

You are given a 2-D array of size ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N)X![equation](http://latex.codecogs.com/svg.latex?\inline&space;M). <br> 
Your task is to find:
1. The mean along axis ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1)
2. The var along axis ![equation](http://latex.codecogs.com/svg.latex?\inline&space;0)
3. The std along axis ![equation](http://latex.codecogs.com/svg.latex?\inline&space;None)

__Input Format__

The first line contains the space separated values of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M). <br>
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M) space separated integers.

__Output Format__

First, print the mean. <br>
Second, print the var. <br>
Third, print the std.

__Sample Input__
```commandline
2 2
1 2
3 4
```
__Sample Output__
```commandline
[ 1.5  3.5]
[ 1.  1.]
1.11803398875
```
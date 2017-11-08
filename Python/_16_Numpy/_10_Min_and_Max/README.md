[min](http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.min.html)

The tool min returns the minimum value along a given axis.
```python
import numpy

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print numpy.min(my_array, axis = 0)         #Output : [1 0]
print numpy.min(my_array, axis = 1)         #Output : [2 3 1 0]
print numpy.min(my_array, axis = None)      #Output : 0
print numpy.min(my_array)                   #Output : 0
```
By default, the axis value is None. Therefore, it finds the minimum over all the dimensions of the input array.

[max](http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.max.html)

The tool max returns the maximum value along a given axis.
```python
import numpy

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print numpy.max(my_array, axis = 0)         #Output : [4 7]
print numpy.max(my_array, axis = 1)         #Output : [5 7 3 4]
print numpy.max(my_array, axis = None)      #Output : 7
print numpy.max(my_array)                   #Output : 7
```
By default, the axis value is None. Therefore, it finds the maximum over all the dimensions of the input array.

__Task__

You are given a 2-D array with dimensions ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N)X![equation](http://latex.codecogs.com/svg.latex?\inline&space;M). <br>
Your task is to perform the min function over axis ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1) and then find the max of that.

__Input Format__

The first line of input contains the space separated values of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M). <br>
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M) space separated integers.

__Output Format__

Compute the min along axis ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1) and then print the max of that result.

__Sample Input__
```commandline
4 2
2 5
3 7
1 3
4 0
```
__Sample Output__
```commandline
3
```
__Explanation__

The min along axis ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1) = ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20%5B2%2C%203%2C%201%2C%200%5D) <br> 
The max of ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20%5B2%2C%203%2C%201%2C%200%5D) = ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3)
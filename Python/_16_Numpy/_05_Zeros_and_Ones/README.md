[zeros]()

The zeros tool returns a new array with a given shape and type filled with ![equation](http://latex.codecogs.com/svg.latex?\inline&space;0)'s.
```python
import numpy

print numpy.zeros((1,2))                    #Default type is float
#Output : [[ 0.  0.]] 

print numpy.zeros((1,2), dtype = numpy.int) #Type changes to int
#Output : [[0 0]]
```
[ones]()

The ones tool returns a new array with a given shape and type filled with ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1)'s.
```python
import numpy

print numpy.ones((1,2))                    #Default type is float
#Output : [[ 1.  1.]] 

print numpy.ones((1,2), dtype = numpy.int) #Type changes to int
#Output : [[1 1]] 
```  
__Task__

You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.

__Input Format__

A single line containing the space-separated integers.

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20each%5C%20integer%20%5Cleq%203)

__Output Format__

First, print the array using the numpy.zeros tool and then print the array with the numpy.ones tool.

__Sample Input 0__
```commandline
3 3 3
```
__Sample Output 0__
```commandline
[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]
```
__Explanation 0__

Print the array built using numpy.zeros and numpy.ones tools and you get the result as shown.
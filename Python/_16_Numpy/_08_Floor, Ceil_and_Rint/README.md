[floor](http://docs.scipy.org/doc/numpy/reference/generated/numpy.floor.html#numpy-floor) <br>
The tool floor returns the floor of the input element-wise. <br>
The floor of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;x) is the largest integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i) where ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20i%20%5Cleq%20x).
```python
import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.floor(my_array)         #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
```
[ceil](http://docs.scipy.org/doc/numpy/reference/generated/numpy.ceil.html#numpy-ceil) <br>
The tool ceil returns the ceiling of the input element-wise. <br>
The ceiling of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;x) is the smallest integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i) where ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20i%20%5Cgeq%20x).
```python
import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.ceil(my_array)          #[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
```
[rint](http://docs.scipy.org/doc/numpy/reference/generated/numpy.rint.html) <br>
The rint tool rounds to the nearest integer of input element-wise.
```python
import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.rint(my_array)          #[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
```
__Task__

You are given a 1-D array, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A). Your task is to print the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;floor), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;ceil) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;rint) of all the elements of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A).

__Input Format__

A single line of input containing the space separated elements of array ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A).

__Output Format__

On the first line, print the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;floor) of A. <br>
On the second line, print the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;ceil) of A. <br>
On the third line, print the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;rint) of A.

__Sample Input__
```commandline
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
```
__Sample Output__
```commandline
[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
```
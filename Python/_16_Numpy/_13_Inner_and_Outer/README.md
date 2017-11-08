[inner](http://docs.scipy.org/doc/numpy/reference/generated/numpy.inner.html)

The inner tool returns the [inner product](https://en.wikipedia.org/wiki/Inner_product_space) of two arrays.
```python
import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.inner(A, B)     #Output : 4
```
[outer](http://docs.scipy.org/doc/numpy/reference/generated/numpy.outer.html)

The outer tool returns the [outer product](https://en.wikipedia.org/wiki/Outer_product) of two arrays.
```python
import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.outer(A, B)     #Output : [[0 0]
                            #          [3 4]]
```
__Task__

You are given two arrays: ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B). <br>
Your task is to compute their inner and outer product.

__Input Format__

The first line contains the space separated elements of array ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A). <br>
The second line contains the space separated elements of array ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B).

__Output Format__

First, print the inner product. <br>
Second, print the outer product.

__Sample Input__
```commandline
0 1
2 3
```
__Sample Output__
```commandline
3
[[0 0]
 [2 3]]
```
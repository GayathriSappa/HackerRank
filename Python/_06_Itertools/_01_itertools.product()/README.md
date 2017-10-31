[itertools.product()](https://docs.python.org/2/library/itertools.html#itertools.product)

This tool computes the [cartesian product](https://en.wikipedia.org/wiki/Cartesian_product) of input iterables. <br> 
It is equivalent to nested for-loops. <br> 
For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

__Sample Code__
```python
>>> from itertools import product
>>>
>>> print list(product([1,2,3],repeat = 2))
[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
>>>
>>> print list(product([1,2,3],[3,4]))
[(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]
>>>
>>> A = [[1,2,3],[3,4,5]]
>>> print list(product(*A))
[(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)]
>>>
>>> B = [[1,2,3],[3,4,5],[7,8]]
>>> print list(product(*B))
[(1, 3, 7), (1, 3, 8), (1, 4, 7), (1, 4, 8), (1, 5, 7), (1, 5, 8), (2, 3, 7), (2, 3, 8), (2, 4, 7), (2, 4, 8), (2, 5, 7), (2, 5, 8), (3, 3, 7), (3, 3, 8), (3, 4, 7), (3, 4, 8), (3, 5, 7), (3, 5, 8)]
```
__Task__

You are given a two lists ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B). Your task is to compute their cartesian product [AXB](https://en.wikipedia.org/wiki/Cartesian_product).

__Example__
```python
A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
```
__Note:__ ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B) are sorted lists, and the cartesian product's tuples should be output in sorted order.

__Input Format__

The first line contains the space separated elements of list ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A). <br> 
The second line contains the space separated elements of list ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B).

Both lists have no duplicate integer elements.

__Constraints__

 ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20A%20%3C%2030)<br>
 ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20B%20%3C%2030)

__Output Format__

Output the space separated tuples of the cartesian product.

__Sample Input__
```commandline
 1 2
 3 4
```
__Sample Output__
```commandline
 (1, 3) (1, 4) (2, 3) (2, 4)
```
[itertools.combinations(iterable, r)](https://docs.python.org/2/library/itertools.html#itertools.combinations)

This tool returns the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;r) length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

__Sample Code__
```python
>>> from itertools import combinations
>>> 
>>> print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
>>> 
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,4))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]
```
__Task__

You are given a string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S). <br> 
Your task is to print all possible combinations, up to size ![equation](http://latex.codecogs.com/svg.latex?\inline&space;k), of the string in lexicographic sorted order.

__Input Format__

A single line containing the string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S) and integer value ![equation](http://latex.codecogs.com/svg.latex?\inline&space;k) separated by a space.

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20k%20%5Cleq%20len%28S%29) <br>
The string contains only UPPERCASE characters.

__Output Format__

Print the different combinations of string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S) on separate lines.

__Sample Input__
```commandline
HACK 2
```
__Sample Output__
```commandline
A
C
H
K
AC
AH
AK
CH
CK
HK
```
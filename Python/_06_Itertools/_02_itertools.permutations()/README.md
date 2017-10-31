[itertools.permutations(iterable[, r])](https://docs.python.org/2/library/itertools.html#itertools.permutations)

This tool returns successive ![equation](http://latex.codecogs.com/svg.latex?\inline&space;r) length permutations of elements in an iterable.

If ![equation](http://latex.codecogs.com/svg.latex?\inline&space;r) is not specified or is None, then ![equation](http://latex.codecogs.com/svg.latex?\inline&space;r) defaults to the length of the iterable, and all possible full length permutations are generated.

Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.

__Sample Code__
```python
>>> from itertools import permutations
>>> print permutations(['1','2','3'])
<itertools.permutations object at 0x02A45210>
>>> 
>>> print list(permutations(['1','2','3']))
[('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
>>> 
>>> print list(permutations(['1','2','3'],2))
[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
>>>
>>> print list(permutations('abc',3))
[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
```
__Task__

You are given a string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S). <br>
Your task is to print all possible permutations of size ![equation](http://latex.codecogs.com/svg.latex?\inline&space;k) of the string in lexicographic sorted order.

__Input Format__

A single line containing the space separated string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S) and the integer value ![equation](http://latex.codecogs.com/svg.latex?\inline&space;k).

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20k%20%5Cleq%20len%28S%29)<br>
The string contains only UPPERCASE characters.

__Output Format__

Print the permutations of the string  on separate lines.

__Sample Input__
```commandline
HACK 2
```
__Sample Output__
```commandline
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
```
__Explanation__

All possible size ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) permutations of the string __"HACK"__ are printed in lexicographic sorted order.
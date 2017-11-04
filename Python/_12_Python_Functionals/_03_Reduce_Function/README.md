Given a list of rational numbers,find their product.

__Concept__

The reduce() function applies a function of two arguments cumulatively on a list of objects in succession from left to right to reduce it to one value. Say you have a list, say [1,2,3] and you have to find its sum.
```python
>>> reduce(lambda x, y : x + y,[1,2,3])
6
```
You can also define an initial value. If it is specified, the function will assume initial value as the value given, and then reduce. It is equivalent to adding the initial value at the beginning of the list. For example:
```python
>>> reduce(lambda x, y : x + y, [1,2,3], -3)
3

>>> from fractions import gcd
>>> reduce(gcd, [2,4,8], 3)
1
```
__Input Format__

First line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n), the number of rational numbers. <br>
The ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i^{th}) of next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) lines contain two integers each, the numerator( ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N_i) ) and denominator( ![equation](http://latex.codecogs.com/svg.latex?\inline&space;D_i) ) of the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i^{th}) rational number in the list.

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%5Cleq%20n%20%5Cleq%20100)
* ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%5Cleq%20N_i%2C%20D_i%20%5Cleq%2010%5E9)

__Output Format__

Print only one line containing the numerator and denominator of the product of the numbers in the list in its simplest form, i.e. numerator and denominator have no common divisor other than ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1).

__Sample Input 0__
```commandline
3
1 2
3 4
10 6
```
__Sample Output 0__
```commandline
5 8
```
__Explanation 0__

Required product is ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20%5Cfrac%7B1%7D%7B2%7D%5Cfrac%7B3%7D%7B4%7D%5Cfrac%7B10%7D%7B6%7D%20%3D%20%5Cfrac%7B5%7D%7B8%7D)
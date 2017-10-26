We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

Let's try to understand this with an example.

You are given an immutable string, and you want to make changes to it.

__Example__
```python
>>> string = "abracadabra"
```
You can access an index by:
```python
>>> print string[5]
a
```
What if you would like to assign a value?
```python
>>> string[5] = 'k' 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```
How would you approach this?

* One solution is to convert the string to a list and then change the value.

__Example__
```python
>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra
```
* Another approach is to slice the string and join it back.

__Example__
```python
>>> string = string[:5] + "k" + string[6:]
>>> print string
abrackdabra
```
__Task__<br> 
Read a given string, change the character at a given index and then print the modified string.

__Input Format__<br> 
The first line contains a string, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S).<br> 
The next line contains an integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i), denoting the index location and a character ![equation](http://latex.codecogs.com/svg.latex?\inline&space;c) separated by a space.

__Output Format__<br> 
Using any of the methods explained above, replace the character at index ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i) with character ![equation](http://latex.codecogs.com/svg.latex?\inline&space;c).

__Sample Input__
```commandline
abracadabra
5 k
```
__Sample Output__
```commandline
abrackdabra
```
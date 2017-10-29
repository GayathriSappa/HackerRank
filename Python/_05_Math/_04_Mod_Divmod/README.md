One of the built-in functions of Python is divmod, which takes two arguments ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b) and returns a tuple containing the quotient of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a/b) first and then the remainder ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a).

For example:
```python
>>> print divmod(177,10)
(17, 7)
```
Here, the integer division is 177/10 => 17 and the modulo operator is 177%10 => 7.

__Task__<br> 
Read in two integers, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b), and print three lines.<br> 
The first line is the integer division ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a//b) (While using Python2 remember to import division from __future__).<br> 
The second line is the result of the modulo operator: ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20a%5C%25b).<br> 
The third line prints the divmod of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b).

__Input Format__<br> 
The first line contains the first integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a), and the second line contains the second integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b).

__Output Format__<br> 
Print the result as described above.

__Sample Input__
```commandline
177
10
```
S__ample Output__
```commandline
17
7
(17, 7)
```
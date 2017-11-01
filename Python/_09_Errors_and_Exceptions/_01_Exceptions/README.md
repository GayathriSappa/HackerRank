[Exceptions](https://docs.python.org/2/tutorial/errors.html#exceptions)

Errors detected during execution are called exceptions.

__Examples:__

[ZeroDivisionError](https://docs.python.org/2/library/exceptions.html#exceptions.ZeroDivisionError)<br> 
This error is raised when the second argument of a division or modulo operation is zero.
```python
>>> a = '1'
>>> b = '0'
>>> print int(a) / int(b)
>>> ZeroDivisionError: integer division or modulo by zero
```
[ValueError](https://docs.python.org/2/library/exceptions.html#exceptions.ValueError)<br> 
This error is raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.
```python
>>> a = '1'
>>> b = '#'
>>> print int(a) / int(b)
>>> ValueError: invalid literal for int() with base 10: '#'
```
To learn more about different built-in exceptions [click here](https://docs.python.org/2/library/exceptions.html#module-exceptions).

[Handling Exceptions](https://docs.python.org/2/tutorial/errors.html#handling-exceptions)

The statements try and except can be used to handle selected exceptions. A try statement may have more than one except clause to specify handlers for different exceptions.
```python
#Code
try:
    print 1/0
except ZeroDivisionError as e:
    print "Error Code:",e
```
__Output__

Error Code: integer division or modulo by zero

__Task__

You are given two values ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b). <br> 
Perform integer division and print ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a/b).

__Input Format__

The first line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;T), the number of test cases. <br> 
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;T) lines each contain the space separated values of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b).

__Constraints__

* ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20T%20%3C%2010)

__Output Format__

Print the value of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a/b). <br> 
In the case of ZeroDivisionError or ValueError, print the error code.

__Sample Input__
```commandline
3
1 0
2 $
3 1
```
__Sample Output__
```commandline
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
```
__Note:__<br> 
For integer division in __Python 3__ use //.
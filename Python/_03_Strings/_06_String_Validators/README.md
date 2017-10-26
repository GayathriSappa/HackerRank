Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

[str.isalnum()](https://docs.python.org/2/library/stdtypes.html#str.isalnum)<br> 
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
```python
>>> print 'ab123'.isalnum()
True
>>> print 'ab123#'.isalnum()
False
```
[str.isalpha()](https://docs.python.org/2/library/stdtypes.html#str.isalpha)<br> 
This method checks if all the characters of a string are alphabetical (a-z and A-Z).
```python
>>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False
```
[str.isdigit()](https://docs.python.org/2/library/stdtypes.html#str.isdigit)<br>
This method checks if all the characters of a string are digits (0-9).
```python
>>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False
```
[str.islower()](https://docs.python.org/2/library/stdtypes.html#str.islower)<br>
This method checks if all the characters of a string are lowercase characters (a-z).
```python
>>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False
```
[str.isupper()]()<br>
This method checks if all the characters of a string are uppercase characters (A-Z).
```python
>>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
False
```
__Task__

You are given a string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S).<br> 
Your task is to find out if the string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S) contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

__Input Format__

A single line containing a string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S).

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?\inline&space;0&space;<&space;len(S)&space;<&space;100)

__Output Format__

In the first line, print True if ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S) has any alphanumeric characters. Otherwise, print False. 
In the second line, print True if ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S) has any alphabetical characters. Otherwise, print False. 
In the third line, print True if ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S) has any digits. Otherwise, print False. 
In the fourth line, print True if ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S) has any lowercase characters. Otherwise, print False. 
In the fifth line, print True if ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S) has any uppercase characters. Otherwise, print False.

__Sample Input__
```commandline
qA2
```
__Sample Output__
```commandline
True
True
True
True
True
```
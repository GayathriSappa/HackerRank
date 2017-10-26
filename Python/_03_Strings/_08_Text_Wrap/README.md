[Textwrap](https://docs.python.org/2/library/textwrap.html#module-textwrap)

The textwrap module provides two convenient functions: wrap() and fill().

[textwrap.wrap()](https://docs.python.org/2/library/textwrap.html#textwrap.wrap)<br> 
The wrap() function wraps a single paragraph in text (a string) so that every line is width characters long at most. 
It returns a list of output lines.
```python
>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.wrap(string,8)
['This is', 'a very', 'very', 'very', 'very', 'very', 'long', 'string.']
``` 
[textwrap.fill()](https://docs.python.org/2/library/textwrap.html#textwrap.fill)<br> 
The fill() function wraps a single paragraph in text and returns a single string containing the wrapped paragraph.
```python
>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.fill(string,8)
This is
a very
very
very
very
very
long
string.
```
__Task__

You are given a string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S) and width ![equation](http://latex.codecogs.com/svg.latex?\inline&space;w).<br> 
Your task is to wrap the string into a paragraph of width ![equation](http://latex.codecogs.com/svg.latex?\inline&space;w).

__Input Format__

The first line contains a string, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S).<br> 
The second line contains the width, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;w).

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?\inline&space;0&space;<&space;len(S)&space;<&space;1000)<br>
![equation](https://latex.codecogs.com/svg.latex?\inline&space;0&space;<&space;w&space;<&space;len(S)) 

__Output Format__

Print the text wrapped paragraph.

__Sample Input__
```commandline
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
```
__Sample Output__
```commandline
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ  
```
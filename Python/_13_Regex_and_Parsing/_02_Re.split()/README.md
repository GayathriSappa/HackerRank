[re.split()](https://docs.python.org/2/library/re.html#re.split)

The re.split() expression splits the string by occurrence of a pattern.

__Code__
```python
>>> import re
>>> re.split("-","+91-011-2711-1111")
['+91', '011', '2711', '1111']
```
__Task__ <br> 
You are given a string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S), containing , and/or . and 0-9 digits. <br>
Your task is to re.split() all of the , and . symbols.

__Input Format__

A single line of input containing the string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S).

__Output Format__

Print the numbers obtained after splitting the string on separate lines.

__Sample Input__
```commandline
100,000,000.000
```
__Sample Output__
```commandline
100
000
000
000
```
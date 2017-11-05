[re](https://docs.python.org/2/library/re.html#module-re)

A regular expression (or RegEx) specifies a set of strings that matches it.

A [regex](https://en.wikipedia.org/wiki/Regular_expression) is a sequence of characters that defines a search pattern, mainly for the use of string pattern matching.


The [re.search()](https://docs.python.org/2/library/re.html#re.search) expression scans through a string looking for the first location where the regex pattern produces a match. 
It either returns a MatchObject instance or returns None if no position in the string matches the pattern.

__Code__

```python
>>> import re
>>> print bool(re.search(r"ly","similarly"))
True
```

The [re.match()](https://docs.python.org/2/library/re.html#re.match) expression only matches at the beginning of the string. 
It either returns a MatchObject instance or returns None if the string does not match the pattern. 

__Code__

```python
>>> import re
>>> print bool(re.match(r"ly","similarly"))
False
>>> print bool(re.match(r"ly","ly should be in the beginning"))
True
```
__Task__<br>
You are given a string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N). <br>
Your task is to verify that ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) is a floating point number.

In this task, a valid float number must satisfy all of the following requirements:

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20%3E) Number can start with +, - or . symbol. <br> 
For example: <br>
✔+4.50 <br>
✔-1.0 <br>
✔.5 <br>
✔-.7 <br>
✔+.4 <br>
✖-+4.5

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20%3E) Number must contain at least ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1) decimal value. <br>
For example: <br>
✖12. <br>
✔12.0  

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20%3E) Number must have exactly one . symbol. <br>
![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20%3E) Number must not give any exceptions when converted using ![equation](http://latex.codecogs.com/svg.latex?\inline&space;float(N)).

__Input Format__

The first line contains an integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;T), the number of test cases. 
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;T) line(s) contains a string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N).

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20T%20%3C%2010)

__Output Format__

Output True or False for each test case.

__Sample Input__
```commandline
4  
4.0O0
-1.00
+4.54
SomeRandomStuff
```
__Sample Output__
```commandline
False
True
True
False
```
__Explanation__

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%204.0O0): O is not a digit. <br>
![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20-1.00): is valid. <br>
![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20&plus;4.54): is valid. <br>
SomeRandomStuff: is not a number.
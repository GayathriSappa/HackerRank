[re.findall()](https://docs.python.org/2/library/re.html#re.findall)

The expression re.findall() returns all the non-overlapping matches of patterns in a string as a list of strings. <br>
__Code__
```python
>>> import re
>>> re.findall(r'\w','http://www.hackerrank.com/')
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
```
[re.finditer()](https://docs.python.org/2/library/re.html#re.finditer)

The expression re.finditer() returns an iterator yielding MatchObject instances over all non-overlapping matches for the re pattern in the string. <br>
__Code__
```python
>>> import re
>>> re.finditer(r'\w','http://www.hackerrank.com/')
<callable-iterator object at 0x0266C790>
>>> map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
```
__Task__ <br> 
You are given a string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S). It consists of alphanumeric characters, spaces and symbols(+,-). <br>
Your task is to find all the substrings of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S) that contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) or more vowels. <br>
Also, these substrings must lie in between ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) consonants and should contain vowels only.

Note : <br>
Vowels are defined as: AEIOU and aeiou. <br>
Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.

__Input Format__

A single line of input containing string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S).

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20len%28S%29%20%3C%20100)

__Output Format__

Print the matched substrings in their order of occurrence on separate lines. 
If no match is found, print -1.

__Sample Input__
```commandline
rabcdeefgyYhFjkIoomnpOeorteeeeet
```
__Sample Output__
```commandline
ee
Ioo
Oeo
eeeee
```
__Explanation__

__ee__ is located between consonant ![equation](http://latex.codecogs.com/svg.latex?\inline&space;d) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;f). <br>
__Ioo__ is located between consonant ![equation](http://latex.codecogs.com/svg.latex?\inline&space;k) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;m). <br>
__Oeo__ is located between consonant ![equation](http://latex.codecogs.com/svg.latex?\inline&space;p) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;r). <br>
__eeeee__ is located between consonant ![equation](http://latex.codecogs.com/svg.latex?\inline&space;t) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;t).
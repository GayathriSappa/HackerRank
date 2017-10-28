__.difference()__

The tool .difference() returns a set with all the elements from the set that are not in an iterable.<br>
Sometimes the - operator is used in place of the .difference() tool, but it only operates on the set of elements in set.<br>
Set is immutable to the .difference() operation (or the - operation).
```python
>>> s = set("Hacker")
>>> print s.difference("Rank")
set(['c', 'r', 'e', 'H'])

>>> print s.difference(set(['R', 'a', 'n', 'k']))
set(['c', 'r', 'e', 'H'])

>>> print s.difference(['R', 'a', 'n', 'k'])
set(['c', 'r', 'e', 'H'])

>>> print s.difference(enumerate(['R', 'a', 'n', 'k']))
set(['a', 'c', 'r', 'e', 'H', 'k'])

>>> print s.difference({"Rank":1})
set(['a', 'c', 'e', 'H', 'k', 'r'])

>>> s - set("Rank")
set(['H', 'c', 'r', 'e'])
```
__Task__

Students of District College have a subscription to English and French newspapers. Some students have subscribed to only the English newspaper, some have subscribed to only the French newspaper, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to only English newspapers.

__Input Format__

The first line contains the number of students who have subscribed to the English newspaper.<br> 
The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.<br>
The third line contains the number of students who have subscribed to the French newspaper.<br> 
The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20Total%5C%20number%5C%20of%5C%20students%5C%20in%5C%20college%20%3C%201000)

__Output Format__

Output the total number of students who are subscribed to the English newspaper only.

__Sample Input__
```commandline
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
```
__Sample Output__
```commandline
4
```
__Explanation__

The roll numbers of students who only have English newspaper subscriptions are:<br>
![equation](https://latex.codecogs.com/svg.latex?\inline&space;4,&space;5,&space;7) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;9).<br>
Hence, the total is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4) students.

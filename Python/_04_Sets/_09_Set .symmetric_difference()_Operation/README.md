__.symmetric_difference()__

The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.<br>
Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.<br>
The set is immutable to the .symmetric_difference() operation (or ^ operation).
```python
>>> s = set("Hacker")
>>> print s.symmetric_difference("Rank")
set(['c', 'e', 'H', 'n', 'R', 'r'])

>>> print s.symmetric_difference(set(['R', 'a', 'n', 'k']))
set(['c', 'e', 'H', 'n', 'R', 'r'])

>>> print s.symmetric_difference(['R', 'a', 'n', 'k'])
set(['c', 'e', 'H', 'n', 'R', 'r'])

>>> print s.symmetric_difference(enumerate(['R', 'a', 'n', 'k']))
set(['a', 'c', 'e', 'H', (0, 'R'), 'r', (2, 'n'), 'k', (1, 'a'), (3, 'k')])

>>> print s.symmetric_difference({"Rank":1})
set(['a', 'c', 'e', 'H', 'k', 'Rank', 'r'])

>>> s ^ set("Rank")
set(['c', 'e', 'H', 'n', 'R', 'r'])
```
__Task__

Students of District College have subscriptions to English and French newspapers. Some students have subscribed to English only, some have subscribed to French only, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.

__Input Format__

The first line contains the number of students who have subscribed to the English newspaper.<br> 
The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.<br>
The third line contains the number of students who have subscribed to the French newspaper.<br> 
The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20Total%5C%20number%5C%20of%5C%20students%5C%20in%5C%20college%20%3C%201000)

__Output Format__

Output total number of students who have subscriptions to the English or the French newspaper but not both.

__Sample Input__
```commandline
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
```
__Sample Output__
```commandline
8
```
__Explanation__

The roll numbers of students who have subscriptions to English or French newspapers but not both are:<br>
![equation](https://latex.codecogs.com/svg.latex?\inline&space;4,&space;5,&space;7,&space;9,&space;10,&space;11,&space;21) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;55).<br>
Hence, the total is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;8) students.

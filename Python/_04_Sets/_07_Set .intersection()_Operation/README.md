__.intersection()__

The .intersection() operator returns the intersection of a set and the set of elements in an iterable.<br>
Sometimes, the & operator is used in place of the .intersection() operator, but it only operates on the set of elements in set.<br>
The set is immutable to the .intersection() operation (or & operation).
```python
>>> s = set("Hacker")
>>> print s.intersection("Rank")
set(['a', 'k'])

>>> print s.intersection(set(['R', 'a', 'n', 'k']))
set(['a', 'k'])

>>> print s.intersection(['R', 'a', 'n', 'k'])
set(['a', 'k'])

>>> print s.intersection(enumerate(['R', 'a', 'n', 'k']))
set([])

>>> print s.intersection({"Rank":1})
set([])

>>> s & set("Rank")
set(['a', 'k'])
```
__Task__
The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.

__Input Format__

The first line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n), the number of students who have subscribed to the English newspaper.<br> 
The second line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) space separated roll numbers of those students.<br>
The third line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b), the number of students who have subscribed to the French newspaper.<br> 
The fourth line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) space separated roll numbers of those students.

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20Total%5C%20number%5C%20of%5C%20students%5C%20in%5C%20college%20%3C%201000)

__Output Format__

Output the total number of students who have subscriptions to __both__ English and French newspapers.

__Sample Input__
```commandline
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
```
__Sample Output__
```commandline
5
```
__Explanation__

The roll numbers of students who have both subscriptions:<br>
![equation](https://latex.codecogs.com/svg.latex?\inline&space;1,&space;2,&space;3,&space;6) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;8).<br>
Hence, the total is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;5) students.

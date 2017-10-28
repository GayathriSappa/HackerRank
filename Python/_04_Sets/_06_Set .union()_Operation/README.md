![](https://github.com/avtomato/HackerRank/blob/master/Python/img/1437829708-707212e33e-AuB.png)

__.union()__

The .union() operator returns the union of a set and the set of elements in an iterable. 
Sometimes, the | operator is used in place of .union() operator, but it operates only on the set of elements in set.
Set is immutable to the .union() operation (or | operation).

__Example__
```python
>>> s = set("Hacker")
>>> print s.union("Rank")
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print s.union(set(['R', 'a', 'n', 'k']))
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print s.union(['R', 'a', 'n', 'k'])
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print s.union(enumerate(['R', 'a', 'n', 'k']))
set(['a', 'c', 'r', 'e', (1, 'a'), (2, 'n'), 'H', 'k', (3, 'k'), (0, 'R')])

>>> print s.union({"Rank":1})
set(['a', 'c', 'r', 'e', 'H', 'k', 'Rank'])

>>> s | set("Rank")
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])
```
__Task__
The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.

__Input Format__

The first line contains an integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n), the number of students who have subscribed to the English newspaper.<br> 
The second line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) space separated roll numbers of those students.<br> 
The third line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b), the number of students who have subscribed to the French newspaper.<br> 
The fourth line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b) space separated roll numbers of those students.

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20Total%5C%20number%5C%20of%5C%20students%5C%20in%5C%20college%20%3C%201000)

__Output Format__

Output the total number of students who have at least one subscription.

__Sample Input__
```commandline
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
```
__Sample Output__
```commandline
13
```
__Explanation__

Roll numbers of students who have at least one subscription:<br>
![equation](https://latex.codecogs.com/svg.latex?\inline&space;1,&space;2,&space;3,&space;4,&space;5,&space;6,&space;7,&space;8,&space;9,&space;10,&space;11,&space;21) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;55). Roll numbers: ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1,&space;2,&space;3,&space;6) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;8) are in both sets so they are only counted once.
Hence, the total is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;13) students.

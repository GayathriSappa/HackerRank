We have seen the applications of union, intersection, difference and symmetric difference operations, but these operations do not make any changes or mutations to the set.

__We can use the following operations to create mutations to a set:__

__.update()__ or __|=__<br> 
Update the set by adding elements from an iterable/another set.
```python
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.update(R)
>>> print H
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
```
__.intersection_update()__ or __&=__<br>
Update the set by keeping only the elements found in it and an iterable/another set.
```python
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.intersection_update(R)
>>> print H
set(['a', 'k'])
```
__.difference_update()__ or __-=__<br>
Update the set by removing elements found in an iterable/another set.
```python
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.difference_update(R)
>>> print H
set(['c', 'e', 'H', 'r'])
```
__.symmetric_difference_update()__ or __^=__<br>
Update the set by only keeping the elements found in either set, but not in both.
```python
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.symmetric_difference_update(R)
>>> print H
set(['c', 'e', 'H', 'n', 'r', 'R'])
```
__TASK__<br>
You are given a set  and  number of other sets. These  number of sets have to perform some specific mutation operations on set .

Your task is to execute those operations and print the sum of elements from set .

__Input Format__

The first line contains the number of elements in set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A).<br>
The second line contains the space separated list of elements in set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A).<br>
The third line contains integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N), the number of other sets.<br>
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2*N) lines are divided into ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) parts containing two lines each.<br>
The first line of each part contains the space separated entries of the operation name and the length of the other set.<br>
The second line of each part contains space separated list of elements in the other set.

![equation](http://latex.codecogs.com/svg.latex?\inline&space;0<) len(set(A))![equation](http://latex.codecogs.com/svg.latex?\inline&space;<1000)  
![equation](http://latex.codecogs.com/svg.latex?\inline&space;0<) len(otherSets)![equation](http://latex.codecogs.com/svg.latex?\inline&space;<100)  
![equation](https://latex.codecogs.com/svg.latex?\inline&space;0&space;<&space;N&space;<&space;100)

__Output Format__

Output the sum of elements in set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A).

__Sample Input__
```commandline
 16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66
```
__Sample Output__
```commandline
38
```
__Explanation__

After the first operation, (intersection_update operation), we get:<br>
set ![equation](https://latex.codecogs.com/svg.latex?\inline&space;A&space;=&space;set([1,&space;2,&space;3,&space;4,&space;5,&space;6,&space;7,&space;8,&space;9,&space;11]))

After the second operation, (update operation), we get:<br>
set ![equation](https://latex.codecogs.com/svg.latex?\inline&space;A&space;=&space;set([1,&space;2,&space;3,&space;4,&space;5,&space;6,&space;7,&space;8,&space;9,&space;11,&space;55,&space;66]))

After the third operation, (symmetric_difference_update operation), we get:<br>
set ![equation](https://latex.codecogs.com/svg.latex?\inline&space;A&space;=&space;set([1,&space;2,&space;3,&space;4,&space;5,&space;6,&space;8,&space;9,&space;11,&space;22,&space;35,&space;55,&space;58,&space;62,&space;66]))

After the fourth operation, ( difference_update operation), we get:<br>
set ![equation](https://latex.codecogs.com/svg.latex?\inline&space;A&space;=&space;set([1,&space;2,&space;3,&space;4,&space;5,&space;6,&space;8,&space;9))

The sum of elements in set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) after these operations is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;38).
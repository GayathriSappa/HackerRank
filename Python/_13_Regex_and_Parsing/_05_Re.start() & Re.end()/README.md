[start() & end()](https://docs.python.org/2/library/re.html#re.MatchObject.start)

These expressions return the indices of the start and end of the substring matched by the group.

__Code__

```python
>>> import re
>>> m = re.search(r'\d+','1234')
>>> m.end()
4
>>> m.start()
0
```
__Task__ <br>
You are given a string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S). <br>
Your task is to find the indices of the start and end of string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;k) in ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S).

__Input Format__

The first line contains the string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S). <br>
The second line contains the string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;k).

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20len%28S%29%20%3C%20100) <br>
![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20len%28k%29%20%3C%20len%28S%29)

__Output Format__

Print the tuple in this format: (start _index, end _index). 
If no match is found, print (-1, -1).

__Sample Input__
```commandline
aaadaa
aa
```
__Sample Output__
```commandline
(0, 1)  
(1, 2)
(4, 5)
```
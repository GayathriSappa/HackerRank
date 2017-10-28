If we want to add a single element to an existing set, we can use the .add() operation.<br> 
It adds the element to the set and returns __'None'__.

__Example__
```python
>>> s = set('HackerRank')
>>> s.add('H')
>>> print s
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
>>> print s.add('HackerRank')
None
>>> print s
set(['a', 'c', 'e', 'HackerRank', 'H', 'k', 'n', 'r', 'R'])
```
__Task__

Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) country stamps.

Find the total number of distinct country stamps.

__Input Format__

The first line contains an integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N), the total number of country stamps.<br>
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines contains the name of the country where the stamp is from.
 
__Constraints__

![equation](https://latex.codecogs.com/svg.latex?\inline&space;0&space;<&space;N&space;<&space;100)

__Output Format__

Output the total number of distinct country stamps on a single line.

__Sample Input__
```commandline
7
UK
China
USA
France
New Zealand
UK
France
``` 
__Sample Output__
```commandline
5
```
__Explanation__

UK and France repeat twice. Hence, the total number of distinct country stamps is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;5) (five).
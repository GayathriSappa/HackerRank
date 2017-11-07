[collections.deque()](https://docs.python.org/2/library/collections.html#collections.deque)

A deque is a double-ended queue. It can be used to add or remove elements from both ends.

Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same ![equation](http://latex.codecogs.com/svg.latex?\inline&space;O(1)) performance in either direction.

Click on the link to learn more about [deque() methods](https://docs.python.org/2/library/collections.html#deque-objects). <br>
Click on the link to learn more about various approaches to working with deques: [Deque Recipes](https://docs.python.org/2.7/library/collections.html#deque-recipes).

__Example__

*__Code__*
```python
>>> from collections import deque
>>> d = deque()
>>> d.append(1)
>>> print d
deque([1])
>>> d.appendleft(2)
>>> print d
deque([2, 1])
>>> d.clear()
>>> print d
deque([])
>>> d.extend('1')
>>> print d
deque(['1'])
>>> d.extendleft('234')
>>> print d
deque(['4', '3', '2', '1'])
>>> d.count('1')
1
>>> d.pop()
'1'
>>> print d
deque(['4', '3', '2'])
>>> d.popleft()
'4'
>>> print d
deque(['3', '2'])
>>> d.extend('7896')
>>> print d
deque(['3', '2', '7', '8', '9', '6'])
>>> d.remove('2')
>>> print d
deque(['3', '7', '8', '9', '6'])
>>> d.reverse()
>>> print d
deque(['6', '9', '8', '7', '3'])
>>> d.rotate(3)
>>> print d
deque(['8', '7', '3', '6', '9'])
```
__Task__

Perform append, pop, popleft and appendleft methods on an empty deque ![equation](http://latex.codecogs.com/svg.latex?\inline&space;d).

__Input Format__

The first line contains an integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N), the number of operations. <br>
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines contains the space separated names of methods and their values.

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20N%20%5Cleq%20100)

__Output Format__

Print the space separated elements of deque ![equation](http://latex.codecogs.com/svg.latex?\inline&space;d).

__Sample Input__
```commandline
6
append 1
append 2
append 3
appendleft 4
pop
popleft
```
__Sample Output__
```commandline
1 2
```
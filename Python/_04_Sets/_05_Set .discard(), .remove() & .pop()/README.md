__.remove(x)__

This operation removes element ![equation](http://latex.codecogs.com/svg.latex?\inline&space;x) from the set.<br> 
If element ![equation](http://latex.codecogs.com/svg.latex?\inline&space;x) does not exist, it raises a __KeyError__.<br>
The .remove(x) operation returns __None__.

__Example__
```python
>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.remove(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.remove(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.remove(0)
KeyError: 0
```
__.discard(x)__

This operation also removes element ![equation](http://latex.codecogs.com/svg.latex?\inline&space;x) from the set.<br> 
If element ![equation](http://latex.codecogs.com/svg.latex?\inline&space;x) does not exist, it __does__ not raise a KeyError.<br>
The .discard(x) operation returns __None__.

__Example__
```python
>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.discard(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.discard(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.discard(0)
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
```
__.pop()__
This operation removes and return an arbitrary element from the set.<br> 
If there are no elements to remove, it raises a __KeyError__.

__Example__
```python
>>> s = set([1])
>>> print s.pop()
1
>>> print s
set([])
>>> print s.pop()
KeyError: pop from an empty set
```
__Task__

You have a non-empty set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s), and you have to execute ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) commands given in ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines.

The commands will be pop, remove and discard.

__Input Format__

The first line contains integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n), the number of elements in the set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s).<br> 
The second line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) space separated elements of set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s). All of the elements are non-negative integers, less than or equal to 9.<br> 
The third line contains integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N), the number of commands.<br>
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines contains either pop, remove and/or discard commands followed by their associated value.

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?\inline&space;0&space;<&space;n&space;<&space;20)<br>
![equation](https://latex.codecogs.com/svg.latex?\inline&space;0&space;<&space;N&space;<&space;20)

__Output Format__

Print the sum of the elements of set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s) on a single line.

__Sample Input__
```commandline
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5
```
__Sample Output__
```commandline
4
```
__Explanation__

After completing these ![equation](http://latex.codecogs.com/svg.latex?\inline&space;10) operations on the set, we get set![equation](http://latex.codecogs.com/svg.latex?\inline&space;([4])). Hence, the sum is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4).

__Note:__ Convert the elements of set s to integers while you are assigning them. To ensure the proper input of the set, we have added the first two lines of code to the editor.
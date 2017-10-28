__Objective__<br> 
Today, we're learning about a new data type: sets.

__Concept__

If the inputs are given on one line separated by a space character, use split() to get the separate values in the form of a list:
```python
>> a = raw_input()
5 4 3 2
>> lis = a.split()
>> print (lis)
['5', '4', '3', '2']
```
If the list values are all integer types, use the map() method to convert all the strings to integers.
```python
>> newlis = list(map(int, lis))
>> print (newlis)
[5, 4, 3, 2]
```
Sets are an unordered bag of unique values. A single set contains values of any immutable data type. 

__CREATING SETS__
```python
>> myset = {1, 2} # Directly assigning values to a set
>> myset = set()  # Initializing a set
>> myset = set(['a', 'b']) # Creating a set from a list
>> myset
{'a', 'b'}
```
__MODIFYING SETS__

Using the add() function:
```python
>> myset.add('c')
>> myset
{'a', 'c', 'b'}
>> myset.add('a') # As 'a' already exists in the set, nothing happens
>> myset.add((5, 4))
>> myset
{'a', 'c', 'b', (5, 4)}
```
Using the update() function:
```python
>> myset.update([1, 2, 3, 4]) # update() only works for iterable objects
>> myset
{'a', 1, 'c', 'b', 4, 2, (5, 4), 3}
>> myset.update({1, 7, 8})
>> myset
{'a', 1, 'c', 'b', 4, 7, 8, 2, (5, 4), 3}
>> myset.update({1, 6}, [5, 13])
>> myset
{'a', 1, 'c', 'b', 4, 5, 6, 7, 8, 2, (5, 4), 13, 3}
```
__REMOVING ITEMS__ 

Both the discard() and remove() functions take a single value as an argument and removes that value from the set. If that value is not present, discard() does nothing, but remove() will raise a KeyError exception.
```python
>> myset.discard(10)
>> myset
{'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 13, 11, 3}
>> myset.remove(13)
>> myset
{'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 11, 3}
```
__COMMON SET OPERATIONS__ 

Using union(), intersection() and difference() functions. 
```python
>> a = {2, 4, 5, 9}
>> b = {2, 4, 11, 12}
>> a.union(b) # Values which exist in a or b
{2, 4, 5, 9, 11, 12}
>> a.intersection(b) # Values which exist in a and b
{2, 4}
>> a.difference(b) # Values which exist in a but not in b
{9, 5}
```
The union() and intersection() functions are symmetric methods: 
```python
>> a.union(b) == b.union(a)
True
>> a.intersection(b) == b.intersection(a)
True
>> a.difference(b) == b.difference(a)
False
```
These [other built-in data structures in Python](http://www.thelearningpoint.net/computer-science/learning-python-programming-and-data-structures/learning-python-programming-and-data-structures--tutorial-4--built-in-data-structures-strings-lists-tuples-dictionaries-mutability) are also useful.

__Task__ 
Given ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) sets of integers, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N), print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M) or ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) but do not exist in both.

__Input Format__

The first line of input contains an integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M).<br> 
The second line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M) space-separated integers.<br> 
The third line contains an integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N).<br> 
The fourth line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) space-separated integers.<br>

__Output Format__

Output the symmetric difference integers in ascending order, one per line.

__Sample Input__
```commandline
4
2 4 5 9
4
2 4 11 12
```
__Sample Output__
```commandline
5
9
11
12
```
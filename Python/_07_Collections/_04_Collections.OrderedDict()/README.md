[collections.OrderedDict](https://docs.python.org/2/library/collections.html#ordereddict-objects)

An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.

__Example__

*__Code__*
```python
>>> from collections import OrderedDict
>>> 
>>> ordinary_dictionary = {}
>>> ordinary_dictionary['a'] = 1
>>> ordinary_dictionary['b'] = 2
>>> ordinary_dictionary['c'] = 3
>>> ordinary_dictionary['d'] = 4
>>> ordinary_dictionary['e'] = 5
>>> 
>>> print ordinary_dictionary
{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
>>> 
>>> ordered_dictionary = OrderedDict()
>>> ordered_dictionary['a'] = 1
>>> ordered_dictionary['b'] = 2
>>> ordered_dictionary['c'] = 3
>>> ordered_dictionary['d'] = 4
>>> ordered_dictionary['e'] = 5
>>> 
>>> print ordered_dictionary
OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
```
__Task__

You are the manager of a supermarket. <br>
You have a list of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) items together with their prices that consumers bought on a particular day. <br>
Your task is to print each item_name and net_price in order of its first occurrence.

```commandline
item_name = Name of the item. 
net_price = Quantity of the item sold multiplied by the price of each item.
```

__Input Format__

The first line contains the number of items, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N). <br> 
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines contains the item's name and price, separated by a space.

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20N%20%5Cleq%20100)

__Output Format__

Print the item_name and net_price in order of its first occurrence.

__Sample Input__
```commandline
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
```
__Sample Output__
```commandline
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
```
__Explanation__

_BANANA FRIES_: Quantity bought: ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1), Price: ![equation](http://latex.codecogs.com/svg.latex?\inline&space;12) <br> 
Net Price: ![equation](http://latex.codecogs.com/svg.latex?\inline&space;12) <br> 
_POTATO CHIPS_: Quantity bought: ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2), Price: ![equation](http://latex.codecogs.com/svg.latex?\inline&space;30) <br>
Net Price: ![equation](http://latex.codecogs.com/svg.latex?\inline&space;60) <br> 
_APPLE JUICE_: Quantity bought: ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2), Price: ![equation](http://latex.codecogs.com/svg.latex?\inline&space;10) <br> 
Net Price: ![equation](http://latex.codecogs.com/svg.latex?\inline&space;20) <br>
_CANDY_: Quantity bought: ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4), Price: ![equation](http://latex.codecogs.com/svg.latex?\inline&space;5) <br> 
Net Price: ![equation](http://latex.codecogs.com/svg.latex?\inline&space;20)
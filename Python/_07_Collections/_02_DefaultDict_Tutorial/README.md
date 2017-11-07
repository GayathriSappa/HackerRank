The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but it has one difference: The value fields' data type is specified upon initialization. 

__For example__:
```python
from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i
```
This prints:
```python
('python', ['awesome', 'language'])
('something-else', ['not relevant'])
```
In this challenge, you will be given ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) integers, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;m). There are ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) words, which might repeat, in word group ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A). There are ![equation](http://latex.codecogs.com/svg.latex?\inline&space;m) words belonging to word group ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B). For each ![equation](http://latex.codecogs.com/svg.latex?\inline&space;m) words, check whether the word has appeared in group ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) or not. Print the indices of each occurrence of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;m) in group ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A). If it does not appear, print ![equation](http://latex.codecogs.com/svg.latex?\inline&space;-1).

__Constraints__ 
 
 ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20n%20%5Cleq%2010000) <br>
 ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20m%20%5Cleq%20100) <br>
 ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20length%5C%20of%5C%20each%5C%20word%5C%20in%5C%20the%5C%20input%20%5Cleq%20100)

__Input Format__

The first line contains integers, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;m) separated by a space. <br>
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) lines contains the words belonging to group ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A). <br>
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;m) lines contains the words belonging to group ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B).

__Output Format__

Output ![equation](http://latex.codecogs.com/svg.latex?\inline&space;m) lines. <br>
The ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i^{th}) line should contain the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1)-indexed positions of the occurrences of the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i^{th}) word separated by spaces.

__Sample Input__
```commandline
5 2
a
a
b
a
b
a
b
```
__Sample Output__
```commandline
1 2 4
3 5
```
__Explanation__

__'a'__ appeared ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3) times in positions ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4). <br>
__'b'__ appeared ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) times in positions ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;5). <br>
In the sample problem, if __'c'__ also appeared in word group ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B), you would print ![equation](http://latex.codecogs.com/svg.latex?\inline&space;-1).
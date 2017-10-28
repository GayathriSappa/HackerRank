A set is an unordered collection of elements without duplicate entries.<br> 
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

__Example__
```python
>>> print set()
set([])

>>> print set('HackerRank')
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

>>> print set([1,2,1,2,3,4,5,6,0,9,12,22,3])
set([0, 1, 2, 3, 4, 5, 6, 9, 12, 22])

>>> print set((1,2,3,4,5,5))
set([1, 2, 3, 4, 5])

>>> print set(set(['H','a','c','k','e','r','r','a','n','k']))
set(['a', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print set({'Hacker' : 'DOSHI', 'Rank' : 616 })
set(['Hacker', 'Rank'])

>>> print set(enumerate(['H','a','c','k','e','r','r','a','n','k']))
set([(6, 'r'), (7, 'a'), (3, 'k'), (4, 'e'), (5, 'r'), (9, 'k'), (2, 'c'), (0, 'H'), (1, 'a'), (8, 'n')])

```
Basically, sets are used for membership testing and eliminating duplicate entries. 

__Task__

Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Formula used:

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20Average%20%3D%5Cfrac%7BSum%5C%20of%5C%20Distinct%5C%20Heights%7D%7BTotal%5C%20Number%5C%20of%5C%20Distinct%5C%20Heights%7D)

__Input Format__

The first line contains the integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N), the total number of plants.
The second line contains the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) space separated heights of the plants.

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?\inline&space;0&space;<&space;N&space;\leq&space;100)

__Output Format__

Output the average height value on a single line.

__Sample Input__
```commandline
10
161 182 161 154 176 170 167 171 170 174
```
__Sample Output__
```commandline
169.375
```
__Explanation__

Here, set ![equation](https://latex.codecogs.com/svg.latex?\inline&space;([154,&space;161,&space;167,&space;170,&space;171,&space;174,&space;176,&space;182])) is the set containing the distinct heights. Using the sum() and len() functions, we can compute the average.

![equation](https://latex.codecogs.com/svg.latex?\inline&space;Average&space;=&space;\frac{1355}{8}&space;=&space;169.375)

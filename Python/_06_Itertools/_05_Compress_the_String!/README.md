In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, [Check this out](https://docs.python.org/2/library/itertools.html#itertools.groupby).

You are given a string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S). Suppose a character '![equation](http://latex.codecogs.com/svg.latex?\inline&space;c)' occurs consecutively ![equation](http://latex.codecogs.com/svg.latex?\inline&space;X) times in the string. Replace these consecutive occurrences of the character '![equation](http://latex.codecogs.com/svg.latex?\inline&space;c)' with ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20%28X%2C%20c%29) in the string.

For a better understanding of the problem, check the explanation.

__Input Format__

A single line of input consisting of the string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S).

__Output Format__

A single line of output consisting of the modified string.

__Constraints__

All the characters of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S) denote integers between ![equation](http://latex.codecogs.com/svg.latex?\inline&space;0) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;9).

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20%7CS%7C%20%5Cleq%2010%5E4)

__Sample Input__
```commandline
1222311
```
__Sample Output__
```commandline
(1, 1) (3, 2) (1, 3) (2, 1)
```
__Explanation__

First, the character ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1) occurs only once. It is replaced by ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20%281%2C%201%29). Then the character ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) occurs three times, and it is replaced by ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20%283%2C%202%29) and so on.

Also, note the single space within each compression and between the compressions.
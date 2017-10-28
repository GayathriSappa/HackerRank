You are given two sets, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B).<br> 
Your job is to find whether set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) is a subset of set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B).

If set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) is subset of set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B), print __True__.<br>
If set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) is not a subset of set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B), print __False__.

__Input Format__

The first line will contain the number of test cases, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n).<br> 
The first line of each test case contains the number of elements in set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A).<br>
The second line of each test case contains the space separated elements of set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A).<br>
The third line of each test case contains the number of elements in set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B).<br>
The fourth line of each test case contains the space separated elements of set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B).

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?\inline&space;0&space;<&space;T&space;<&space;21)<br>
![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20Number%5C%20of%5C%20elements%5C%20of%5C%20each%5C%20set%20%3C%201001)

__Output Format__

Output __True__ or __False__ for each test case on separate lines.

Sample Input
```commandline
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
```
Sample Output
```commandline
True 
False
False
```
__Explanation__

__Test Case 01 Explanation__

Set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) = {1 2 3 5 6}<br> 
Set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B) = {9 8 5 6 3 2 1 4 7}<br> 
All the elements of set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) are elements of set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B).<br> 
Hence, set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) is a subset of set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B).


__Note: More than 4 lines will result in a score of zero. Blank lines won't be counted__.

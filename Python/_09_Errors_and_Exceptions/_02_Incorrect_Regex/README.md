You are given a string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S). <br> 
Your task is to find out whether ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S) is a valid [regex](https://en.wikipedia.org/wiki/Regular_expression) or not.

__Input Format__

The first line contains integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;T), the number of test cases. <br>
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;T) lines contains the string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S).

__Constraints__

* ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20T%20%3C%20100)

__Output Format__

Print "True" or "False" for each test case without quotes.

__Sample Input__
```commandline
2
.*\+
.*+
```
__Sample Output__
```commandline
True
False
```
__Explanation__

__.*\\+__ : Valid regex. <br> 
__.*+__ : Has the error multiple repeat. Hence, it is invalid.
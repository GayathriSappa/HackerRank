You are given a string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S) which contains only lowercase English characters. <br>
Your task is to find the top three most common characters in the string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S).

__Input Format__

A single line of input containing the string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S).

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%203%20%5Cleq%20len%28S%29%20%5Cleq%2010%5E4)

__Output Format__

Print the three most common characters along with their occurrence count each on a separate line. <br>
Sort output in descending order of occurrence count. <br>
If the occurrence count is the same, sort the characters in ascending order.

__Sample Input 0__
```commandline
aabbbccde
```
__Sample Output 0__
```commandline
b 3
a 2
c 2
```
__Explanation 0__

Here, b occurs ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3) times. It is printed first. <br>
Both a and c occur ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) times. So, a is printed in the second line and c in the third line because a comes before c.

__Note__: The string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S) has at least ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3) distinct characters.
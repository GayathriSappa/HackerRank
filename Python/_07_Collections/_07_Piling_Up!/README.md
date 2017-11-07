There is a horizontal row of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if ![equation](http://latex.codecogs.com/svg.latex?\inline&space;cube_i) is on top of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;cube_j) then ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20sideLength_j%20%5Cgeq%20sideLength_i).

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.

__Input Format__

The first line contains a single integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;T), the number of test cases. <br>
For each test case, there are ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) lines. <br>
The first line of each test case contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n), the number of cubes. <br>
The second line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) space separated integers, denoting the sideLengths of each cube in that order.

__Constraints__
 
 ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20T%20%5Cleq%205) <br>
 ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20n%20%5Cleq%2010%5E5) <br>
 ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20sideLength%20%3C%202%5E%7B31%7D)

__Output Format__

For each test case, output a single line containing either "Yes" or "No" without the quotes.

__Sample Input__
```commandline
2
6
4 3 2 1 3 4
3
1 3 2
```
__Sample Output__
```commandline
Yes
No
```
__Explanation__

In the first test case, pick in this order: __left -__ ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4), __right -__ ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4), __left -__ ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3), __right -__ ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3), __left -__ ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2), __right -__ ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1). <br>
In the second test case, no order gives an appropriate arrangement of vertical cubes. ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3) will always come after either ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1) or ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2).
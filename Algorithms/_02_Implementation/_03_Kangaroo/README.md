There are two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity). The first kangaroo starts at location ![equation](http://latex.codecogs.com/svg.latex?\inline&space;x_1) and moves at a rate of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;v_1) meters per jump. The second kangaroo starts at location ![equation](http://latex.codecogs.com/svg.latex?\inline&space;x_2) and moves at a rate of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;v_2) meters per jump. Given the starting locations and movement rates for each kangaroo, can you determine if they'll ever land at the same location at the same time?

__Input Format__

A single line of four space-separated integers denoting the respective values of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;x_1), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;v_1), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;x_2), and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;v_2).

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;0\leq&space;x_1&space;<&space;x_2&space;\leq&space;10000)
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\le&space;v_1&space;\le&space;10000)
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\le&space;v_2&space;\le&space;10000)

__Output Format__

Print YES if they can land on the same location at the same time; otherwise, print NO.

__Note:__ The two kangaroos must land at the same location after making the same number of jumps.

__Sample Input 0__
```commandline
0 3 4 2
```
__Sample Output 0__
```commandline
YES
```
__Explanation 0__

The two kangaroos jump through the following sequence of locations:

Thus, the kangaroos meet after ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4) jumps and we print YES.

__Sample Input 1__
```commandline
0 2 5 3
```
__Sample Output 1__
```commandline
NO
```
__Explanation 1__

The second kangaroo has a starting location that is ahead (further to the right) of the first kangaroo's starting location (i.e., ![equation](https://latex.codecogs.com/svg.latex?\inline&space;x_2&space;>&space;x_1)). Because the second kangaroo moves at a faster rate (meaning ![equation](https://latex.codecogs.com/svg.latex?\inline&space;v_2&space;>&space;v_1)) and is already ahead of the first kangaroo, the first kangaroo will never be able to catch up. Thus, we print NO.
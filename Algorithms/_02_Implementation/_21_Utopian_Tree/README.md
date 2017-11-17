The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.

Laura plants a Utopian Tree sapling with a height of 1 meter at the onset of spring. How tall will her tree be after ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) growth cycles?

__Input Format__

The first line contains an integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;T), the number of test cases.<br> 
![equation](http://latex.codecogs.com/svg.latex?\inline&space;T) subsequent lines each contain an integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N), denoting the number of cycles for that test case.

__Constraints__ 
 
![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\leq&space;T&space;\leq&space;10)<br>
![equation](https://latex.codecogs.com/svg.latex?\inline&space;0&space;\leq&space;N&space;\leq&space;60)

__Output Format__

For each test case, print the height of the Utopian Tree after ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) cycles. Each height must be printed on a new line.

__Sample Input__
```commandline
3
0
1
4
```
__Sample Output__
```commandline
1
2
7
```
__Explanation__

There are 3 test cases.

In the first case (![equation](https://latex.codecogs.com/svg.latex?\inline&space;N&space;=&space;0)), the initial height (![equation](https://latex.codecogs.com/svg.latex?\inline&space;H&space;=&space;1)) of the tree remains unchanged.

In the second case (![equation](https://latex.codecogs.com/svg.latex?\inline&space;N&space;=&space;1)), the tree doubles in height and is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) meters tall after the spring cycle.

In the third case (![equation](https://latex.codecogs.com/svg.latex?\inline&space;N&space;=&space;4)), the tree doubles its height in spring (![equation](https://latex.codecogs.com/svg.latex?\inline&space;H&space;=&space;2)), then grows a meter in summer (![equation](https://latex.codecogs.com/svg.latex?\inline&space;H&space;=&space;3)), then doubles after the next spring (![equation](https://latex.codecogs.com/svg.latex?\inline&space;H&space;=&space;6)), and grows another meter after summer (![equation](https://latex.codecogs.com/svg.latex?\inline&space;H&space;=&space;7)). Thus, at the end of 4 cycles, its height is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;7) meters.
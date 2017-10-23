Emma is playing a new mobile game involving ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) clouds numbered from ![equation](http://latex.codecogs.com/svg.latex?\inline&space;0) to ![equation](https://latex.codecogs.com/svg.latex?\inline&space;n&space;-&space;1). A player initially starts out on cloud ![equation](http://latex.codecogs.com/svg.latex?\inline&space;c_0), and they must jump to cloud ![equation](http://latex.codecogs.com/svg.latex?\inline&space;c_{n-1}). In each step, she can jump from any cloud ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i) to cloud ![equation](https://latex.codecogs.com/svg.latex?\inline&space;i&space;&plus;&space;1) or cloud ![equation](https://latex.codecogs.com/svg.latex?\inline&space;i&space;&plus;&space;2).

There are two types of clouds, ordinary clouds and thunderclouds. The game ends if Emma jumps onto a thundercloud, but if she reaches the last cloud (i.e., ![equation](http://latex.codecogs.com/svg.latex?\inline&space;c_{n-1})), she wins the game!

![](https://github.com/avtomato/HackerRank/blob/master/Algorithms/img/1461134431-8156ea51b7-jump1.png)

Can you find the minimum number of jumps Emma must make to win the game? It is guaranteed that clouds ![equation](http://latex.codecogs.com/svg.latex?\inline&space;c_0) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;c_{n-1}) are ordinary-clouds and it is always possible to win the game.

__Input Format__

The first line contains an integer, ![equation](https://latex.codecogs.com/svg.latex?\inline&space;n) (the total number of clouds).<br> 
The second line contains ![equation](https://latex.codecogs.com/svg.latex?\inline&space;n) space-separated binary integers describing clouds .

* If ![equation](https://latex.codecogs.com/svg.latex?\inline&space;c_i&space;&plus;&space;0), the ![equation](https://latex.codecogs.com/svg.latex?\inline&space;i^{th}) cloud is an ordinary cloud.
* If ![equation](https://latex.codecogs.com/svg.latex?\inline&space;c_i&space;&plus;&space;1), the ![equation](https://latex.codecogs.com/svg.latex?\inline&space;i^{th}) cloud is a thundercloud.

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;2&space;\leq&space;n&space;\leq&space;100)
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;c_i&space;\in&space;\left&space;\{&space;0,1&space;\right&space;\})
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;c_0&space;=&space;c_{n-1}&space;=&space;0)

__Output Format__

Print the minimum number of jumps needed to win the game.

__Sample Input 0__
```commandline
7
0 0 1 0 0 1 0
```
__Sample Output 0__
```commandline
4
```
__Sample Input 1__
```commandline
6
0 0 0 0 1 0
```
__Sample Output 1__
```commandline
3
```
__Explanation__

Sample Case 0:<br> 
Because ![equation](http://latex.codecogs.com/svg.latex?\inline&space;c_2) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;c_5) in our input are both ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1), Emma must avoid ![equation](http://latex.codecogs.com/svg.latex?\inline&space;c_2) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;c_5). Bearing this in mind, she can win the game with a minimum of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4) jumps:

![](https://github.com/avtomato/HackerRank/blob/master/Algorithms/img/1461134731-c258160d15-jump2.png)

Sample Case 1:<br> 
The only thundercloud to avoid is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;c_4). Emma can win the game in ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3) jumps:

![](https://github.com/avtomato/HackerRank/blob/master/Algorithms/img/1461136358-764298d363-jump5.png)


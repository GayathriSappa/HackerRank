You are given an array of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) integers, ![equation](https://latex.codecogs.com/svg.latex?\inline&space;a_0,&space;a_1,&space;...,&space;a_{n-1}), and a positive integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;k). Find and print the number of ![equation](https://latex.codecogs.com/svg.latex?\inline&space;(i,j)) pairs where ![equation](https://latex.codecogs.com/svg.latex?\inline&space;i&space;<&space;j) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a_i) + ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a_j) is divisible by ![equation](http://latex.codecogs.com/svg.latex?\inline&space;k).

__Input Format__

The first line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) space-separated integers, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;k), respectively. 
The second line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) space-separated integers describing the respective values of ![equation](https://latex.codecogs.com/svg.latex?\inline&space;a_0,&space;a_1,&space;...,&space;a_{n-1}).

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;2&space;\leq&space;n&space;\leq&space;100)
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\le&space;k&space;\le&space;100)
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\le&space;a_i&space;\le&space;100)

__Output Format__

Print the number of ![equation](https://latex.codecogs.com/svg.latex?\inline&space;(i,j)) pairs where ![equation](https://latex.codecogs.com/svg.latex?\inline&space;i&space;<&space;j) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a_i) + ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a_j) is evenly divisible by ![equation](http://latex.codecogs.com/svg.latex?\inline&space;k).

__Sample Input__
```commandline
6 3
1 3 2 6 1 2
```
__Sample Output__
```commandline
 5
```
__Explanation__

Here are the  valid pairs:
* ![equation](https://latex.codecogs.com/gif.latex?\inline&space;(0,&space;2)&space;\rightarrow&space;a_0&space;&plus;&space;a_2&space;=&space;1&space;&plus;&space;2&space;=&space;3)
* ![equation](https://latex.codecogs.com/gif.latex?\inline&space;(0,&space;5)&space;\rightarrow&space;a_0&space;&plus;&space;a_5&space;=&space;1&space;&plus;&space;2&space;=&space;3)
* ![equation](https://latex.codecogs.com/gif.latex?\inline&space;(1,&space;3)&space;\rightarrow&space;a_1&space;&plus;&space;a_3&space;=&space;3&space;&plus;&space;6&space;=&space;9)
* ![equation](https://latex.codecogs.com/gif.latex?\inline&space;(2,&space;4)&space;\rightarrow&space;a_2&space;&plus;&space;a_4&space;=&space;2&space;&plus;&space;1&space;=&space;3)
* ![equation](https://latex.codecogs.com/gif.latex?\inline&space;(4,&space;5)&space;\rightarrow&space;a_4&space;&plus;&space;a_5&space;=&space;1&space;&plus;&space;2&space;=&space;3)
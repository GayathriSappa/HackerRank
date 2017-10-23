John works at a clothing store and he's going through a pile of socks to find the number of matching pairs. More specifically, he has a pile of ![equation](https://latex.codecogs.com/svg.latex?\inline&space;n) loose socks where each sock ![equation](https://latex.codecogs.com/svg.latex?\inline&space;i) is labeled with an integer, ![equation](https://latex.codecogs.com/svg.latex?\inline&space;c_i), denoting its color. He wants to sell as many socks as possible, but his customers will only buy them in matching pairs. Two socks, ![equation](https://latex.codecogs.com/svg.latex?\inline&space;i) and ![equation](https://latex.codecogs.com/svg.latex?\inline&space;j), are a single matching pair if they have the same color (![equation](https://latex.codecogs.com/svg.latex?\inline&space;c_i&space;=&space;c_j)).

Given  and the color of each sock, how many pairs of socks can John sell?

__Input Format__

The first line contains an integer, ![equation](https://latex.codecogs.com/svg.latex?\inline&space;n), denoting the number of socks. 
The second line contains ![equation](https://latex.codecogs.com/svg.latex?\inline&space;n) space-separated integers describing the respective values of ![equation](https://latex.codecogs.com/svg.latex?\inline&space;c_0,&space;c_1,&space;c_2,&space;...,&space;c_{n-1}).

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\leq&space;n&space;\leq&space;100)
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\leq&space;c_i&space;\leq&space;100)

__Output Format__

Print the total number of matching pairs of socks that John can sell.

__Sample Input__
```commandline
9
10 20 20 10 10 30 50 10 20
```
__Sample Output__
```commandline
3
```
__Explanation__

![](https://github.com/avtomato/HackerRank/blob/master/Algorithms/img/1474122392-c7b9097430-sock.png)

As you can see from the figure above, we can match three pairs of socks. Thus, we print ![equation](https://latex.codecogs.com/svg.latex?\inline&space;3) on a new line.
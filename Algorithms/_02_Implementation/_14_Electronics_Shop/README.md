Monica wants to buy exactly one keyboard and one USB drive from her favorite electronics store. The store sells ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) different brands of keyboards and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;m) different brands of USB drives. Monica has exactly ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s) dollars to spend, and she wants to spend as much of it as possible (i.e., the total cost of her purchase must be maximal).

Given the price lists for the store's keyboards and USB drives, find and print the amount money Monica will spend. If she doesn't have enough money to buy one keyboard and one USB drive, print -1 instead.

__Note:__ She will never buy more than one keyboard and one USB drive even if she has the leftover money to do so.

__Input Format__

The first line contains three space-separated integers describing the respective values of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s) (the amount of money Monica has), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) (the number of keyboard brands) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;m) (the number of USB drive brands).<br> 
The second line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) space-separated integers denoting the prices of each keyboard brand.<br> 
The third line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;m) space-separated integers denoting the prices of each USB drive brand.

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\le&space;n,m&space;\le&space;1000)
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\le&space;s&space;\le&space;10^6)
* The price of each item is in the inclusive range ![equation](http://latex.codecogs.com/svg.latex?\inline&space;[1,10^6]).

__Output Format__

Print a single integer denoting the amount of money Monica will spend. If she doesn't have enough money to buy one keyboard and one USB drive, print -1 instead.

__Sample Input 0__
```commandline
10 2 3
3 1
5 2 8
```
__Sample Output 0__
```commandline
9
```
__Explanation 0__

She can buy the ![equation](https://latex.codecogs.com/svg.latex?\inline&space;2^{nd}) keyboard and the ![equation](https://latex.codecogs.com/svg.latex?\inline&space;3^{rd}) USB drive for a total cost of ![equation](https://latex.codecogs.com/svg.latex?\inline&space;8&space;&plus;&space;1&space;=&space;9).

__Sample Input 1__
```commandline
5 1 1
4
5
```
__Sample Output 1__
```commandline
-1
```
__Explanation 1__

There is no way to buy one keyboard and one USB drive because ![equation](https://latex.codecogs.com/svg.latex?\inline&space;4&space;&plus;&space;5&space;>&space;5), so we print ![equation](http://latex.codecogs.com/svg.latex?\inline&space;-1).
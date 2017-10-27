Check [Tutorial](https://www.hackerrank.com/challenges/py-if-else/tutorial) tab to know how to to solve.

__Task__ 

Given an integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n), perform the following conditional actions:
* If ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) is odd, print Weird
* If ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) is even and in the inclusive range of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) to ![equation](http://latex.codecogs.com/svg.latex?\inline&space;5), print Not Weird
* If ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) is even and in the inclusive range of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;6) to ![equation](http://latex.codecogs.com/svg.latex?\inline&space;20), print Weird
* If ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) is even and greater than ![equation](http://latex.codecogs.com/svg.latex?\inline&space;20), print Not Weird

__Input Format__

A single line containing a positive integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n).

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\leq&space;n&space;\leq&space;100)

__Output Format__

Print Weird if the number is weird; otherwise, print Not Weird.

__Sample Input 0__
```commandline
3
```
__Sample Output 0__
```commandline
Weird
```
__Sample Input 1__
```commandline
24
```
__Sample Output 1__
```commandline
Not Weird
```
__Explanation__

Sample Case 0: ![equation](https://latex.codecogs.com/svg.latex?\inline&space;n&space;=&space;3)<br> 
![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) is odd and odd numbers are weird, so we print Weird.

Sample Case 1: ![equation](https://latex.codecogs.com/svg.latex?\inline&space;n&space;=&space;24)  
![equation](https://latex.codecogs.com/svg.latex?\inline&space;n&space;>&space;20) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) is even, so it isn't weird. Thus, we print Not Weird.

Given ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) integers, compute their average correct to three decimal places.

__Input Format__
 
The first line contains an integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N).<br> 
![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines follow, each containing a single integer.

__Output Format__
 
Display the average of the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) integers, rounded off to three decimal places.

__Input Constraints__ 

![equation](https://latex.codecogs.com/svg.latex?\inline&space;1\leq&space;N\leq&space;500) <br>
![equation](https://latex.codecogs.com/svg.latex?\inline&space;-10000&space;\le&space;x&space;\le&space;10000) (![equation](http://latex.codecogs.com/svg.latex?\inline&space;x) refers to elements of the list of integers for which the average is to be computed)

__Sample Input__
```commandline
4
1
2
9
8
```
__Sample Output__
```commandline
5.000
```
__Explanation__
 
The '4' in the first line indicates that there are four integers whose average is to be computed. The average = (1 + 2 + 9 + 8)/4 = 20/4 = 5.000 (correct to three decimal places) Please include the zeroes even if they are redundant (e.g. 0.000 instead of 0).
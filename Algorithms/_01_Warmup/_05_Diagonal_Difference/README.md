Given a square matrix of size ![equation](https://latex.codecogs.com/svg.latex?\inline&space;N&space;\times&space;N), calculate the absolute difference between the sums of its diagonals.

__Input Format__<br>
The first line contains a single integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N). The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines denote the matrix's rows, with each line containing ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) space-separated integers describing the columns.

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;-100&space;\le&space;Elements&space;in&space;the&space;matrix&space;\le&space;100)

__Output Format__<br>
Print the absolute difference between the two sums of the matrix's diagonals as a single integer.

__Sample Input__
```commandline
3
11 2 4
4 5 6
10 8 -12
```
__Sample Output__
```commandline
15
```
__Explanation__<br>
The primary diagonal is:
```commandline
11
   5
     -12
```
Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:
```commandline
     4
   5
10
```
Sum across the secondary diagonal: 4 + 5 + 10 = 19<br> 
Difference: |4 - 19| = 15

Note: |x| is [absolute value](https://www.mathsisfun.com/numbers/absolute-value.html) function

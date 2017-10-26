Given an integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n), print the following values for each integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i) from ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1) to ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n):

1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary

The four values must be printed on a single line in the order specified above for each ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i) from ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1) to ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n). Each value should be space-padded to match the width of the binary value of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n).

__Input Format__

A single integer denoting ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n).

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\leq&space;n&space;\leq&space;99)

__Output Format__

Print ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) lines where each line ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i) (in the range ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\leq&space;i&space;\leq&space;n)) contains the respective decimal, octal, capitalized hexadecimal, and binary values of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i). Each printed value must be formatted to the width of the binary value of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n).

__Sample Input__
```commandline
17
```
__Sample Output__
```commandline

    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001     
```
Given an array of integers, calculate which fraction of its elements are positive, which fraction of its elements are negative, and which fraction of its elements are zeroes, respectively. Print the decimal value of each fraction on a new line.

__Note:__ This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to ![equation](http://latex.codecogs.com/svg.latex?\inline&space;10^{-4}) are acceptable.

__Input Format__<br>
The first line contains an integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N), denoting the size of the array.<br> 
The second line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) space-separated integers describing an array of numbers ![equation](https://latex.codecogs.com/svg.latex?\inline&space;(a_0,&space;a_1,&space;a_2,&space;...,&space;a_{n-1})).

__Output Format__<br>
You must print the following ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3) lines:

1. A decimal representing of the fraction of positive numbers in the array compared to its size.
2. A decimal representing of the fraction of negative numbers in the array compared to its size.
3. A decimal representing of the fraction of zeroes in the array compared to its size.

__Sample Input__
```commandline
6
-4 3 -9 0 4 1
```         
__Sample Output__
```commandline
0.500000
0.333333
0.166667
```
__Explanation__

There are ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3) positive numbers, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) negative numbers, and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1) zero in the array. 
The respective fractions of positive numbers, negative numbers and zeroes are ![equation](https://latex.codecogs.com/svg.latex?\inline&space;\frac{3}{6}&space;=&space;0,500000), ![equation](https://latex.codecogs.com/svg.latex?\inline&space;\frac{2}{6}&space;=&space;0,333333) and ![equation](https://latex.codecogs.com/svg.latex?\inline&space;\frac{1}{6}&space;=&space;0,166667), respectively.
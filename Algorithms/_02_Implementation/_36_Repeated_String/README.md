Lilah has a string, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s), of lowercase English letters that she repeated infinitely many times.

Given an integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n), find and print the number of letter a's in the first ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) letters of Lilah's infinite string.

__Input Format__

The first line contains a single string, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s).<br> 
The second line contains an integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n).

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\le&space;|s|&space;\le&space;100)
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\le&space;n&space;\le&space;10^{12})
* For ![equation](https://latex.codecogs.com/svg.latex?\inline&space;25&space;\%) of the test cases, ![equation](https://latex.codecogs.com/svg.latex?\inline&space;n&space;\le&space;10^6).

__Output Format__

Print a single integer denoting the number of letter a's in the first ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) letters of the infinite string created by repeating ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s) infinitely many times.

__Sample Input 0__
```commandline
aba
10
```
__Sample Output 0__
```commandline
7
```
__Explanation 0__
 
The first ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n&space;=&space;10) letters of the infinite string are abaabaabaa. Because there are ![equation](http://latex.codecogs.com/svg.latex?\inline&space;7) a's, we print ![equation](http://latex.codecogs.com/svg.latex?\inline&space;7) on a new line.

__Sample Input 1__
```commandline
a
1000000000000
```
__Sample Output 1__
```commandline
1000000000000
```
__Explanation 1__
 
Because all of the first ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n&space;=&space;1000000000000) letters of the infinite string are a, we print ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1000000000000) on a new line.
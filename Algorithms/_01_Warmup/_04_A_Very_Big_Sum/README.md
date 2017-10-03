You are given an array of integers of size ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N). You need to print the sum of the elements in the array, keeping in mind that some of those integers may be quite large.

__Input Format__<br>
The first line of the input consists of an integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N). The next line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) space-separated integers contained in the array.

__Output Format__<br>
Print a single value equal to the sum of the elements in the array.

__Constraints__<br> 
![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\le&space;N&space;\le&space;10)<br>
![equation](https://latex.codecogs.com/svg.latex?\inline&space;0&space;\le&space;A[i]&space;\le&space;10^{10}) 

__Sample Input__
```commandline
5
1000000001 1000000002 1000000003 1000000004 1000000005
```
__Output__
```commandline
5000000015
```
__Note:__

The range of the 32-bit integer is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;(-2^{31})&space;to&space;(2^{31})&space;or&space;[-2147483648,&space;2147483647]).

When we add several integer values, the resulting sum might exceed the above range. You might need to use long long int in C/C++ or long data type in Java to store such sums.

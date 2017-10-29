Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is: ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%202%5E%7B31%7D-1) (c++ int) or ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%202%5E%7B63%7D-1) (C++ long long int).

As we know, the result of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a^b) grows really fast with increasing ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b).

Let's do some calculations on very large integers.

__Task__<br> 
Read four numbers, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;c), and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;d), and print the result of ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20a%5Eb%20&plus;%20c%5Ed).

__Input Format__<br> 
Integers ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;c), and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;d) are given on four separate lines, respectively.

__Constraints__ 
 
![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20a%20%5Cleq%201000)<br>
![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20b%20%5Cleq%201000)<br>
![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20c%20%5Cleq%201000)<br>
![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20d%20%5Cleq%201000) 

__Output Format__<br> 
Print the result of ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20a%5Eb%20&plus;%20c%5Ed) on one line.

__Sample Input__
```commandline
9
29
7
27
```
__Sample Output__
```commandline
4710194409608608369201743232
```  
__Note:__ This result is bigger than ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%202%5E%7B63%7D-1). Hence, it won't fit in the long long int of C++ or a 64-bit integer.
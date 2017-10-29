So far, we have only heard of Python's powers. Now, we will witness them!

Powers or exponents in Python can be calculated using the built-in power function. Call the power function ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a^b) as shown below:
```python
>>> pow(a,b)
``` 
or
```python
>>> a**b
```
It's also possible to calculate ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20a%5Eb%5C%20mod%5C%20m).
```python
>>> pow(a,b,m) 
``` 
This is very helpful in computations where you have to print the resultant % mod.

__Note:__ Here, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b) can be floats or negatives, but, if a third argument is present, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b) cannot be negative.

__Note:__ Python has a math module that has its own pow(). It takes two arguments and returns a float. Frankly speaking, we will never use math.pow().

__Task__ 
You are given three integers: ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b), and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;m), respectively. Print two lines. 
The first line should print the result of pow(a,b). The second line should print the result of pow(a,b,m).

__Input Format__<br> 
The first line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a), the second line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b), and the third line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;m).

__Constraints__ 

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20a%20%5Cleq%2010)<br>
![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20b%20%5Cleq%2010)<br>
![equation](https://latex.codecogs.com/svg.latex?%5Cinline%202%20%5Cleq%20m%20%5Cleq%201000)
 

__Sample Input__
```commandline
3
4
5
```
__Sample Output__
```commandline
81
1
```
This challenge is only forPython 2.

[input()](https://docs.python.org/2/library/functions.html#input)

In __Python 2__, the expression input() is equivalent to eval(raw _input(prompt)).

__Code__
```python
>>> input()  
1+2
3
>>> company = 'HackerRank'
>>> website = 'www.hackerrank.com'
>>> input()
'The company name: '+company+' and website: '+website
'The company name: HackerRank and website: www.hackerrank.com'
```
__Task__

You are given a [polynomial](https://en.wikipedia.org/wiki/Polynomial) ![equation](http://latex.codecogs.com/svg.latex?\inline&space;P) of a single indeterminate (or variable), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;x). <br> 
You are also given the values of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;x) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;k). Your task is to verify if ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20P%28x%29%20%3D%20k).

__Constraints__
 
All coefficients of polynomial ![equation](http://latex.codecogs.com/svg.latex?\inline&space;P) are integers. <br>
![equation](http://latex.codecogs.com/svg.latex?\inline&space;x) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;y) are also integers.

__Input Format__

The first line contains the space separated values of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;x) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;k). <br> 
The second line contains the polynomial ![equation](http://latex.codecogs.com/svg.latex?\inline&space;P).

__Output Format__

Print True if ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20P%28x%29%20%3D%20k). Otherwise, print False.

__Sample Input__
```commandline
1 4
x**3 + x**2 + x + 1
```
__Sample Output__
```commandline
True
```
__Explanation__

 ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20P%281%29%20%3D%201%5E3%20&plus;%201%5E2%20&plus;%201%20&plus;%201%20%3D%204%20%3D%20k) <br>
Hence, the output is True.
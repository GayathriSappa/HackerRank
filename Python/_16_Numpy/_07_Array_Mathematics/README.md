Basic mathematical functions operate element-wise on arrays. They are available both as operator overloads and as functions in the NumPy module.
```python
import numpy

a = numpy.array([1,2,3,4], float)
b = numpy.array([5,6,7,8], float)

print a + b                     #[  6.   8.  10.  12.]
print numpy.add(a, b)           #[  6.   8.  10.  12.]

print a - b                     #[-4. -4. -4. -4.]
print numpy.subtract(a, b)      #[-4. -4. -4. -4.]

print a * b                     #[  5.  12.  21.  32.]
print numpy.multiply(a, b)      #[  5.  12.  21.  32.]

print a / b                     #[ 0.2         0.33333333  0.42857143  0.5       ]
print numpy.divide(a, b)        #[ 0.2         0.33333333  0.42857143  0.5       ]

print a % b                     #[ 1.  2.  3.  4.]
print numpy.mod(a, b)           #[ 1.  2.  3.  4.]

print a**b                      #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
print numpy.power(a, b)         #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
```
__Task__

You are given two arrays (![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) & ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B)) of dimensions ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N)X![equation](http://latex.codecogs.com/svg.latex?\inline&space;M). <br>
Your task is to perform the following operations:

1. Add (![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) + ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B))
2. Subtract (![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) - ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B))
3. Multiply (![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) * ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B))
4. Divide (![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) / ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B))
5. Mod (![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) % ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B))
6. Power (![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) ** ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B))

__Input Format__

The first line contains two space separated integers, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M). <br> 
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M) space separated integers of array ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A). <br>
The following ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M) space separated integers of array ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B).

__Output Format__

Print the result of each operation in the given order under __Task__.

__Sample Input__
```commandline
1 4
1 2 3 4
5 6 7 8
```
__Sample Output__
```commandline
[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]] 
```
Use // for division in Python 3.
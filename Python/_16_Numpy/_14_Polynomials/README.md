[poly](http://docs.scipy.org/doc/numpy/reference/generated/numpy.poly.html)

The poly tool returns the coefficients of a polynomial with the given sequence of roots.
```python
print numpy.poly([-1, 1, 1, 10])        #Output : [  1 -11   9  11 -10]
```
[roots](http://docs.scipy.org/doc/numpy/reference/generated/numpy.roots.html)

The roots tool returns the roots of a polynomial with the given coefficients.
```python
print numpy.roots([1, 0, -1])           #Output : [-1.  1.]
```
[polyint](http://docs.scipy.org/doc/numpy/reference/generated/numpy.polyint.html)

The polyint tool returns an antiderivative (indefinite integral) of a polynomial.
```python
print numpy.polyint([1, 1, 1])          #Output : [ 0.33333333  0.5         1.          0.        ]
```
[polyder](http://docs.scipy.org/doc/numpy/reference/generated/numpy.polyder.html#numpy.polyder)

The polyder tool returns the derivative of the specified order of a polynomial.
```python
print numpy.polyder([1, 1, 1, 1])       #Output : [3 2 1]
```
[polyval](http://docs.scipy.org/doc/numpy/reference/generated/numpy.polyval.html#numpy.polyval)

The polyval tool evaluates the polynomial at specific value.
```python
print numpy.polyval([1, -2, 0, 2], 4)   #Output : 34
```
[polyfit](http://docs.scipy.org/doc/numpy/reference/generated/numpy.polyfit.html)

The polyfit tool fits a polynomial of a specified order to a set of data using a least-squares approach.
```python
print numpy.polyfit([0,1,-1, 2, -2], [0,1,1, 4, 4], 2)
#Output : [  1.00000000e+00   0.00000000e+00  -3.97205465e-16]
```
The functions [polyadd](http://docs.scipy.org/doc/numpy/reference/generated/numpy.polyadd.html#numpy.polyadd), [polysub](http://docs.scipy.org/doc/numpy/reference/generated/numpy.polysub.html#numpy.polysub), [polymul](http://docs.scipy.org/doc/numpy/reference/generated/numpy.polymul.html), and [polydiv](http://docs.scipy.org/doc/numpy/reference/generated/numpy.polydiv.html#numpy.polydiv) also handle proper addition, subtraction, multiplication, and division of polynomial coefficients, respectively.

__Task__

You are given the coefficients of a polynomial ![equation](http://latex.codecogs.com/svg.latex?\inline&space;P). <br>
Your task is to find the value of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;P) at point ![equation](http://latex.codecogs.com/svg.latex?\inline&space;x).

__Input Format__

The first line contains the space separated value of the coefficients in ![equation](http://latex.codecogs.com/svg.latex?\inline&space;P). <br>
The second line contains the value of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;x).

__Output Format__

Print the desired value.

__Sample Input__
```commandline
1.1 2 3
0
```
__Sample Output__
```commandline
3.0
```
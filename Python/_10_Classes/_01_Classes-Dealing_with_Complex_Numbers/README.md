For this challenge, you are given two complex numbers, and you have to print the result of their addition, subtraction, multiplication, division and modulus operations.

The real and imaginary precision part should be correct up to two decimal places.

__Input Format__

One line of input: The real and imaginary part of a number separated by a space.

__Output Format__

For two complex numbers ![equation](http://latex.codecogs.com/svg.latex?\inline&space;C) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;D), the output should be in the following sequence on separate lines:
* ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20C%20&plus;%20D)
* ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20C%20-%20D)
* ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20C%20*%20D)
* ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20C%20/%20D)
* ![equation](http://latex.codecogs.com/svg.latex?\inline&space;mod(C))
* ![equation](http://latex.codecogs.com/svg.latex?\inline&space;mod(D))
 
For complex numbers with non-zero real ![equation](http://latex.codecogs.com/svg.latex?\inline&space;(A)) and complex part ![equation](http://latex.codecogs.com/svg.latex?\inline&space;(B)), the output should be in the following format: <br>
![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20A%20&plus;%20Bi) 

Replace the plus symbol ![equation](http://latex.codecogs.com/svg.latex?\inline&space;(+)) with a minus symbol ![equation](http://latex.codecogs.com/svg.latex?\inline&space;(-)) when ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20B%20%3C%200).

For complex numbers with a zero complex part i.e. real numbers, the output should be: <br>
![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20A%20&plus;%200.00i)

For complex numbers where the real part is zero and the complex part is non-zero, the output should be: <br>
![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200.00%20&plus;%20Bi)

__Sample Input__
```commandline
2 1
5 6
```
__Sample Output__
```commandline
7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i
```
__Concept__

Python is a fully object-oriented language like C++, Java, etc. For reading about classes, refer [here](http://www.diveintopython3.net/iterators.html#defining-classes). 

Methods with a double underscore before and after their name are considered as built-in methods. They are used by interpreters and are generally used in the implementation of overloaded operators or other built-in functionality. 

```commandline
__add__-> Can be overloaded for + operation
```

```commandline
__sub__ -> Can be overloaded for - operation
```

```commandline
__mul__ -> Can be overloaded for * operation
```

For more information on operator overloading in Python, refer [here](http://docs.python.org/3.2/reference/datamodel.html).
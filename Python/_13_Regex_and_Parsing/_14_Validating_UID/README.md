ABCXYZ company has up to ![equation](http://latex.codecogs.com/svg.latex?\inline&space;100) employees. <br>
The company decides to create a unique identification number (UID) for each of its employees. <br>
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

* It must contain at least ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) uppercase English alphabet characters.
* It must contain at least ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3) digits (![equation](http://latex.codecogs.com/svg.latex?\inline&space;0) - ![equation](http://latex.codecogs.com/svg.latex?\inline&space;9)).
* It should only contain alphanumeric characters (![equation](http://latex.codecogs.com/svg.latex?\inline&space;a) - ![equation](http://latex.codecogs.com/svg.latex?\inline&space;z), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) - ![equation](http://latex.codecogs.com/svg.latex?\inline&space;Z) & ![equation](http://latex.codecogs.com/svg.latex?\inline&space;0) - ![equation](http://latex.codecogs.com/svg.latex?\inline&space;9)).
* No character should repeat.
* There must be exactly ![equation](http://latex.codecogs.com/svg.latex?\inline&space;10) characters in a valid UID.

__Input Format__

The first line contains an integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;T), the number of test cases. 
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;T) lines contains an employee's UID.

__Output Format__

For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

__Sample Input__
```commandline
2
B1CD102354
B1CDEF2354
```
__Sample Output__
```commandline
Invalid
Valid
```
__Explanation__

__B1CD102354__: ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1) is repeating → Invalid <br>
__B1CDEF2354__: Valid
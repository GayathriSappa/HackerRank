A postal code ![equation](http://latex.codecogs.com/svg.latex?\inline&space;P) must be a number in the range of (![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20100000%20-%20999999)). <br> 
A postal code ![equation](http://latex.codecogs.com/svg.latex?\inline&space;P) must not contain more than one alternating repetitive digit pair. 

Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.

For example:
```commandline
121426 # Here, 1 is an alternating repetitive digit.
523563 # Here, NO digit is an alternating repetitive digit.
552523 # Here, both 2 and 5 are alternating repetitive digits.
```
Your task is to validate whether ![equation](http://latex.codecogs.com/svg.latex?\inline&space;P) is a valid postal code or not.

__Input Format__

One single line of input containing the string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;P).

__Output Format__

Print "True" if ![equation](http://latex.codecogs.com/svg.latex?\inline&space;P) is valid. Otherwise, print "False". Do not print the quotation marks.

__Sample Input 0__
```commandline
110000
```
__Sample Output 0__
```commandline
False
```
__Explanation 0__

1 1 0000 : (0, 0) and (0, 0) are two alternating digit pairs. Hence, it is an invalid postal code.

__Note:__ 
A score of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;0) will be awarded for using 'if' conditions in your code. 
You have to pass all the testcases to get a positive score.
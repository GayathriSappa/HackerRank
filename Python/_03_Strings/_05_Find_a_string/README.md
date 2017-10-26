In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

__NOTE:__ String letters are case-sensitive.

__Input Format__

The first line of input contains the original string. The next line contains the substring.

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\leq&space;len(string)&space;\leq&space;200)<br> 
Each character in the string is an ascii character.

__Output Format__

Output the integer number indicating the total number of occurrences of the substring in the original string.

__Sample Input__
```commandline
ABCDCDC
CDC
```
__Sample Output__
```commandline
2
```
__Concept__

Some string processing examples, [such as these](http://www.thelearningpoint.net/computer-science/learning-python-programming-and-data-structures/learning-python-programming-and-data-structures--tutorial-12--string-manipulation), might be useful.<br> 
There are a couple of new concepts:<br> 
In Python, the length of a string is found by the function len(s), where ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s) is the string.<br> 
To traverse through the length of a string, use a for loop:
```python
for i in range(0, len(s)):
    print (s[i])
```
A range function is used to loop over some length:
```python
range (0, 5)
```
Here, the range loops over ![equation](http://latex.codecogs.com/svg.latex?\inline&space;0) to ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4). ![equation](http://latex.codecogs.com/svg.latex?\inline&space;5) is excluded.
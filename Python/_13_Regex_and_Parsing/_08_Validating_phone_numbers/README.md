Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.

A valid mobile number is a ten digit number starting with a ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%207%2C%208) or ![equation](http://latex.codecogs.com/svg.latex?\inline&space;9).

__Concept__

A valid mobile number is a ten digit number starting with a ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%207%2C%208) or ![equation](http://latex.codecogs.com/svg.latex?\inline&space;9).

Regular expressions are a key concept in any programming language. A quick explanation with Python examples is [available here](http://www.thelearningpoint.net/computer-science/learning-python-programming-and-data-structures/learning-python-programming-and-data-structures--tutorial-13--regular-expression-matching). You could also go through the link below to read more about regular expressions in Python.

https://developers.google.com/edu/python/regular-expressions

__Input Format__

The first line contains an integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N), the number of inputs. <br>
![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines follow, each containing some string.

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20N%20%5Cleq%2010)

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%202%20%5Cleq%20len%28Number%29%20%5Cleq%2015)

__Output Format__

For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.

__Sample Input__
```commandline
2
9587456281
1252478965
```
__Sample Output__
```commandline
YES
NO
```
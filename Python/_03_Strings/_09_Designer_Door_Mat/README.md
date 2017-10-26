Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

* Mat size must be ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N)X![equation](http://latex.codecogs.com/svg.latex?\inline&space;M). (![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) is an odd natural number, and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M) is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3) times ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N).)
* The design should have 'WELCOME' written in the center.
* The design pattern should only use |, . and - characters.

__Sample Designs__
```commandline
    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
```
__Input Format__

A single line containing the space separated values of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M).

Constraints

![equation](https://latex.codecogs.com/svg.latex?\inline&space;5&space;<&space;N&space;<&space;101)<br>
![equation](https://latex.codecogs.com/svg.latex?\inline&space;15&space;<&space;M&space;<&space;303)

__Output Format__

Output the design pattern.

__Sample Input__
```commandline
9 27
```
__Sample Output__
```commandline
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
```
__Note:__<br> 
More than ![equation](http://latex.codecogs.com/svg.latex?\inline&space;6) lines of code will result in a score of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;0). Comment lines are counted. Blank lines are not counted.
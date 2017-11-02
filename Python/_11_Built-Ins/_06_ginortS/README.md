You are given a string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S). <br>
![equation](http://latex.codecogs.com/svg.latex?\inline&space;S) contains alphanumeric characters only. 

![](https://github.com/avtomato/HackerRank/blob/master/Python/img/u7WkSk7.gif)

Your task is to sort the string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S) in the following manner:
* All sorted lowercase letters are ahead of uppercase letters.
* All sorted uppercase letters are ahead of digits.
* All sorted odd digits are ahead of sorted even digits.

__Input Format__

A single line of input contains the string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S).

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20len%28S%29%20%3C%201000)

__Output Format__

Output the sorted string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S).

__Sample Input__
```commandline
Sorting1234
```
__Sample Output__
```commandline
ginortS1324
```
__Note:__<br> 
a) Using join, for or while anywhere in your code, even as substrings, will result in a score of 0. <br> 
b) You can only use ![equation](http://latex.codecogs.com/svg.latex?\inline&space;one) sorted function in your code. A 0 score will be awarded for using sorted more than once. 

__Hint:__ Success is not the key, but ![equation](http://latex.codecogs.com/svg.latex?\inline&space;key) is success.

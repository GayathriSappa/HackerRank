[any()]()

This expression returns True if __any__ element of the iterable is true. <br>
If the iterable is empty, it will return False.

__Code__
```python
>>> any([1>0,1==0,1<0])
True
>>> any([1<0,2<1,3<2])
False
```
[all()]()

This expression returns True if __all__ of the elements of the iterable are true. If the iterable is empty, it will return True.

__Code__
```python
>>> all(['a'<'b','b'<'c'])
True
>>> all(['a'<'b','c'<'b'])
False
```
__Task__

You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a [palindromic integer](https://en.wikipedia.org/wiki/Palindromic_number).

__Input Format__

The first line contains an integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N). ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) is the total number of integers in the list. <br>
The second line contains the space separated list of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) integers.

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20N%20%3C%20100)

__Output Format__

Print True if all the conditions of the problem statement are satisfied. Otherwise, print False.

__Sample Input__
```commandline
5
12 9 61 5 14 
```
__Sample Output__
```commandline
True
```

__Explanation__

__Condition 1:__ All the integers in the list are positive. <br>
__Condition 2:__ 5 is a palindromic integer.

Hence, the output is True.

Can you solve this challenge in 3 lines of code or less? <br>
There is no penalty for solutions that are correct but have more than 3 lines.
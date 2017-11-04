You are given an integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) followed by ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.


Valid email addresses must follow these rules:
* It must have the username@websitename.extension format type.
* The username can only contain letters, digits, dashes and underscores.
* The website name can only have letters and digits.
* The maximum length of the extension is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3). 

__Concept__

A filter takes a function returning True or False and applies it to a sequence, returning a list of only those members of the sequence where the function returned True. A Lambda function can be used with filters. 

Let's say you have to make a list of the squares of integers from ![equation](http://latex.codecogs.com/svg.latex?\inline&space;0) to ![equation](http://latex.codecogs.com/svg.latex?\inline&space;9) (both included).
```python
>> l = list(range(10))
>> l = list(map(lambda x:x*x, l))
```
Now, you only require those elements that are greater than ![equation](http://latex.codecogs.com/svg.latex?\inline&space;10) but less than ![equation](http://latex.codecogs.com/svg.latex?\inline&space;80).
```python
>> l = list(filter(lambda x: x > 10 and x < 80, l))
```
Easy, isn't it?

__Input Format__

The first line of input is the integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N), the number of email addresses.<br> 
![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines follow, each containing a string.

__Constraints__

Each line is a non-empty string.

__Output Format__

Output a list containing the valid email addresses in lexicographical order. If the list is empty, just output an empty list, [].

__Sample Input__
```commandline
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
```
Sample Output
```commandline
['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
```
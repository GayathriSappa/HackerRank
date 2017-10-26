In Python, a string can be split on a delimiter.

__Example:__
```python
>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings. 
>>> print a
['this', 'is', 'a', 'string']
```
Joining a string is simple:
```python
>>> a = "-".join(a)
>>> print a
this-is-a-string 
```
__Task__<br> 
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

__Input Format__<br> 
The first line contains a string consisting of space separated words.

__Output Format__<br> 
Print the formatted string as explained above.

__Sample Input__
```commandline
this is a string 
```  
__Sample Output__
```commandline
this-is-a-string
```
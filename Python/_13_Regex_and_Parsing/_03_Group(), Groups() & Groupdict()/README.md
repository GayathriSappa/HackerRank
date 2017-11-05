[group()](https://docs.python.org/2/library/re.html#re.MatchObject.group)

A group() expression returns one or more subgroups of the match. <br>
__Code__

```python
>>> import re
>>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
>>> m.group(0)       # The entire match 
'username@hackerrank.com'
>>> m.group(1)       # The first parenthesized subgroup.
'username'
>>> m.group(2)       # The second parenthesized subgroup.
'hackerrank'
>>> m.group(3)       # The third parenthesized subgroup.
'com'
>>> m.group(1,2,3)   # Multiple arguments give us a tuple.
('username', 'hackerrank', 'com')
```
[groups()](https://docs.python.org/2/library/re.html#re.MatchObject.groups)

A groups() expression returns a tuple containing all the subgroups of the match. <br>
__Code__

```python
>>> import re
>>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
>>> m.groups()
('username', 'hackerrank', 'com')
```
[groupdict()](https://docs.python.org/2/library/re.html#re.MatchObject.groupdict)

A groupdict() expression returns a dictionary containing all the named subgroups of the match, keyed by the subgroup name. <br>
__Code__

```python
>>> m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
>>> m.groupdict()
{'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}
```
__Task__

You are given a string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S). 
Your task is to find the first occurrence of an alphanumeric character in ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S) (read from left to right) that has consecutive repetitions.

__Input Format__

A single line of input containing the string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S).

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20len%28S%29%20%3C%20100)

Output Format

Print the first occurrence of the repeating character. If there are no repeating characters, print -1.

__Sample Input__
```commandline
..12345678910111213141516171820212223
```
__Sample Output__
```commandline
1
```
__Explanation__

.. is the first repeating character, but it is not alphanumeric. <br>
1 is the first (from left to right) alphanumeric repeating character of the string in the substring 111.
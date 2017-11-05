The re.sub() tool (sub stands for substitution) evaluates a pattern and, for each valid match, it calls a method (or lambda). <br>
The method is called for all matches and can be used to modify strings in different ways. <br>
The re.sub() method returns the modified string as an output.

Learn more about [re.sub()](https://docs.python.org/2/library/re.html#re.sub).

### Transformation of Strings ###

__Code__
```python
import re

#Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number**2)

print re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9")
```
__Output__
```python
1 4 9 16 25 36 49 64 81
```
### Replacements in Strings ###

__Code__
```python
import re

html = """
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie"  value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
"""

print re.sub("(<!--.*?-->)", "", html) #remove comment
```
__Output__
```python
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">

  <param name="quality" value="high"/>
</object>
```
__Task__

You are given a text of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines. The text contains && and || symbols. <br>
Your task is to modify those symbols to the following:
```commandline
&& → and
|| → or
```
Both && and || should have a space " " on both sides.

__Input Format__

The first line contains the integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N). <br> 
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines each contain a line of the text.

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20N%20%3C%20100)

Neither && nor || occur in the start or end of each line.

__Output Format__

Output the modified text.

__Sample Input__
```commandline
11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
```
__Sample Output__
```commandline
a = 1;
b = input();

if a + b > 0 and a - b < 0:
    start()
elif a*b > 10 or a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.  
```
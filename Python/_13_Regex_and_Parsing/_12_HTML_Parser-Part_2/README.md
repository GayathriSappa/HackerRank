*\*This section assumes that you understand the basics discussed in __HTML Parser - Part 1__*

[.handle_comment(data)]()<br> 
This method is called when a comment is encountered (e.g. \<!--comment-->). <br>
The data argument is the content inside the comment tag:

```python
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
          print "Comment  :", data
```

[.handle_data(data)]()<br> 
This method is called to process arbitrary data (e.g. text nodes and the content of \<script>...\</script> and \<style>...\</style>). <br>
The data argument is the text content of HTML.

```python
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        print "Data     :", data
```
__Task__

You are given an HTML code snippet of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines. <br>
Your task is to print the single-line comments, multi-line comments and the data.

Print the result in the following format:
```commandline
>>> Single-line Comment  
Comment
>>> Data                 
My Data
>>> Multi-line Comment  
Comment_multiline[0]
Comment_multiline[1]
>>> Data
My Data
>>> Single-line Comment:
```  
__Note:__ Do not print data if data == '\n'.

__Input Format__

The first line contains integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N), the number of lines in the HTML code snippet. <br>
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines contains HTML code.

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20N%20%3C%20100)

__Output Format__

Print the single-line comments, multi-line comments and the data in order of their occurrence from top to bottom in the snippet.

Format the answers as explained in the problem statement.

__Sample Input__
```commandline
4
<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->
```
__Sample Output__
```commandline
>>> Multi-line Comment
[if IE 9]>IE9-specific content
<![endif]
>>> Data
 Welcome to HackerRank
>>> Single-line Comment
[if IE 9]>IE9-specific content<![endif]
```
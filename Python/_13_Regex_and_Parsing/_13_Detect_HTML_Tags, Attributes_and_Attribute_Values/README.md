You are given an HTML code snippet of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines. <br>
Your task is to detect and print all the HTML tags, attributes and attribute values.

Print the detected items in the following format:

```text
Tag1
Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Tag3
-> Attribute3[0] > Attribute_value3[0]
```

The -> symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute value. <br>
The > symbol acts as a separator of attributes and attribute values.

If an HTML tag has no attribute then simply print the name of the tag.

__Note:__ Do not detect any HTML tag, attribute or attribute value inside the HTML comment tags (\<!-- Comments -->). Comments can be multiline. <br>
All attributes have an attribute value.

__Input Format__

The first line contains an integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N), the number of lines in the HTML code snippet. <br>
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines contain HTML code.

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20N%20%3C%20100)

__Output Format__

Print the HTML tags, attributes and attribute values in order of their occurrence from top to bottom in the snippet.

Format your answers as explained in the problem statement.

__Sample Input__
```commandline
9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
```
__Sample Output__
```commandline
head
title
object
-> type > application/x-flash
-> data > your-file.swf
-> width > 0
-> height > 0
param
-> name > quality
-> value > high
```
__Explanation__

* __head__ tag: Print the head tag only because it has no attribute.

* __title__ tag: Print the title tag only because it has no attribute.

* __object__ tag: Print the object tag. In the next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4) lines, print the attributes type, data, width and                     height along with their respective values.

* __\<!-- Comment -->__ tag: Don't detect anything inside it.

* __param__ tag: Print the param tag. In the next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) lines, print the attributes name along with                     their respective values.
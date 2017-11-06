You are given a valid XML document, and you have to print its score. The score is calculated by the sum of the score of each element. For any element, the score is equal to the number of attributes it has.

__Input Format__

The first line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N), the number of lines in the XML document.<br>
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines follow containing the XML document.

__Output Format__

Output a single line, the integer score of the given XML document.

__Sample Input__
```commandline
6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>
```
__Sample Output__
```commandline
5
```
__Explanation__

The feed and subtitle tag have one attribute each - lang. <br>
The title and updated tags have no attributes. <br>
The link tag has three attributes - rel, type and href. 

So, the total score is ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20&plus;%201%20&plus;%203%20%3D%205). 

There may be any level of nesting in the XML document. To learn about XML parsing, refer [here](http://www.diveintopython3.net/xml.html). 

__NOTE__: In order to parse and generate an XML element tree, use the following code:

```python
>> import xml.etree.ElementTree as etree
>> tree = etree.ElementTree(etree.fromstring(xml))
```
Here, XML is the variable containing the string.<br>
Also, to find the number of keys in a dictionary, use the len function:

```python
>> dicti = {'0': 'This is zero', '1': 'This is one'}
>> print (len(dicti))

2
```
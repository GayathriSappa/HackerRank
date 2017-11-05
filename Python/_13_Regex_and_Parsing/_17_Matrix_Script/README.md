Neo has a complex matrix script. The matrix script is a ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) X ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M) grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

![](https://github.com/avtomato/HackerRank/blob/master/Python/img/1442753362-1075bd12d9-Capture.JPG)

To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.

Neo feels that there is no need to use 'if' conditions for decoding.

Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

__Input Format__

The first line contains space-separated integers ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) (rows) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M) (columns) respectively. <br>
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines contain the row elements of the matrix script.

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20N%2C%20M%20%3C%20100)

__Note:__ A ![equation](http://latex.codecogs.com/svg.latex?\inline&space;0) score will be awarded for using 'if' conditions in your code.

__Output Format__

Print the decoded matrix script.

__Sample Input 0__
```commandline
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!
```
__Sample Output 0__
```commandline
This is Matrix#  %!
```
__Explanation 0__

The decoded script is:
```commandline
This$#is% Matrix#  %!
```
Neo replaces the symbols or spaces between two alphanumeric characters with a single space   ' ' for better readability.

So, the final decoded script is:
```commandline
This is Matrix#  %!
```

[collections.namedtuple()](https://docs.python.org/2/library/collections.html#collections.namedtuple)

Basically, namedtuples are easy to create, lightweight object types. <br>
They turn tuples into convenient containers for simple tasks. <br>
With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

__Example__

*__Code 01__*
```python
>>> from collections import namedtuple
>>> Point = namedtuple('Point','x,y')
>>> pt1 = Point(1,2)
>>> pt2 = Point(3,4)
>>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
>>> print dot_product
11
```
*__Code 02__*
```python
>>> from collections import namedtuple
>>> Car = namedtuple('Car','Price Mileage Colour Class')
>>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
>>> print xyz
Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
>>> print xyz.Class
Y
```
__Task__

Dr. John Wesley has a spreadsheet containing a list of student's ![equation](http://latex.codecogs.com/svg.latex?\inline&space;IDs), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;marks), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;class) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;name).

Your task is to help Dr. Wesley calculate the average marks of the students.

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20Average%20%3D%20%5Cfrac%7BSum%5C%20of%5C%20all%5C%20marks%7D%7BTotal%5C%20students%7D)

*__Note__*: <br>
*__1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet__*. <br>
*__2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)__*

__Input Format__

The first line contains an integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N), the total number of students. <br>
The second line contains the names of the columns in any order. <br>
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines contains the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;marks), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;IDs), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;name) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;class), under their respective column names.

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20N%20%5Cleq%20100)

__Output Format__

Print the average marks of the list corrected to 2 decimal places.

__Sample Input__

*__TESTCASE 01__*
```commandline
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6 
```  
*__TESTCASE 02__*
```commandline
5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5
```
__Sample Output__

*__TESTCASE 01__*
```commandline
78.00
```
*__TESTCASE 02__*
```commandline
81.00
```
__Explanation__

*__TESTCASE 01__*

Average = ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20%2897%20&plus;%2050%20&plus;%2091%20&plus;%2072%20&plus;%2080%29/5)

Can you solve this challenge in 4 lines of code or less? <br>
__NOTE__: There is no penalty for solutions that are correct but have more than 4 lines.
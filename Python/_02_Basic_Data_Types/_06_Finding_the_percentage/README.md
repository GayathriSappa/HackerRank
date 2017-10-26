You have a record of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) followed by the names and marks for ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.

__Input Format__

The first line contains the integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N), the number of students. The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;2&space;\leq&space;N&space;\leq&space;10)
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;0&space;\leq&space;Marks&space;\leq&space;100)

__Output Format__

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

__Sample Input__
```commandline
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
```
__Sample Output__
```commandline
56.00
```
__Explanation__

Marks for Malika are ![equation](https://latex.codecogs.com/svg.latex?\inline&space;\{52,&space;56,&space;60\}) whose average is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;\frac{52&plus;56&plus;60}{3}\Rightarrow&space;56)
HackerLand University has the following grading policy:

* Every student receives a ![equation](https://latex.codecogs.com/svg.latex?\inline&space;grade) in the inclusive range from ![equation](https://latex.codecogs.com/svg.latex?\inline&space;0) to ![equation](https://latex.codecogs.com/svg.latex?\inline&space;100).
* Any ![equation](https://latex.codecogs.com/svg.latex?\inline&space;grade) less than ![equation](https://latex.codecogs.com/svg.latex?\inline&space;40) is a failing grade.

Sam is a professor at the university and likes to round each student's ![equation](https://latex.codecogs.com/svg.latex?\inline&space;grade) according to these rules:

* If the difference between the ![equation](https://latex.codecogs.com/svg.latex?\inline&space;grade) and the next multiple of ![equation](https://latex.codecogs.com/svg.latex?\inline&space;5) is less than ![equation](https://latex.codecogs.com/svg.latex?\inline&space;3), round ![equation](https://latex.codecogs.com/svg.latex?\inline&space;grade) up to the next multiple of ![equation](https://latex.codecogs.com/svg.latex?\inline&space;5).
* If the value of ![equation](https://latex.codecogs.com/svg.latex?\inline&space;grade) is less than ![equation](https://latex.codecogs.com/svg.latex?\inline&space;38), no rounding occurs as the result will still be a failing grade.

For example, ![equation](https://latex.codecogs.com/svg.latex?\inline&space;grade&space;=&space;84) will be rounded to ![equation](https://latex.codecogs.com/svg.latex?\inline&space;85) but ![equation](https://latex.codecogs.com/svg.latex?\inline&space;grade&space;=&space;29) will not be rounded because the rounding would result in a number that is less than ![equation](https://latex.codecogs.com/svg.latex?\inline&space;40).

Given the initial value of ![equation](https://latex.codecogs.com/svg.latex?\inline&space;grade) for each of Sam's ![equation](https://latex.codecogs.com/svg.latex?\inline&space;n) students, write code to automate the rounding process. For each ![equation](https://latex.codecogs.com/svg.latex?\inline&space;grade_i), round it according to the rules above and print the result on a new line.

__Input Format__

The first line contains a single integer denoting ![equation](https://latex.codecogs.com/svg.latex?\inline&space;n) (the number of students).<br> 
Each line ![equation](https://latex.codecogs.com/svg.latex?\inline&space;i) of the ![equation](https://latex.codecogs.com/svg.latex?\inline&space;n) subsequent lines contains a single integer, ![equation](https://latex.codecogs.com/svg.latex?\inline&space;grade_i), denoting student ![equation](https://latex.codecogs.com/svg.latex?\inline&space;i)'s grade.

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\le&space;n&space;\le&space;60)
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;0&space;\le&space;grade_i&space;\le&space;100)

__Output Format__

For each ![equation](https://latex.codecogs.com/svg.latex?\inline&space;grade_i) of the ![equation](https://latex.codecogs.com/svg.latex?\inline&space;n) grades, print the rounded grade on a new line.

__Sample Input 0__
```commandline
4
73
67
38
33
```
__Sample Output 0__
```commandline
75
67
40
33
```
__Explanation 0__

![](https://github.com/avtomato/HackerRank/blob/master/Algorithms/img/1484768684-54439977a1-curving2.png)

1. Student ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1) received a ![equation](https://latex.codecogs.com/svg.latex?\inline&space;73), and the next multiple of ![equation](https://latex.codecogs.com/svg.latex?\inline&space;5) from ![equation](https://latex.codecogs.com/svg.latex?\inline&space;73) is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;75). Since ![equation](https://latex.codecogs.com/svg.latex?\inline&space;75&space;-&space;73&space;<&space;3), the student's grade is rounded to ![equation](https://latex.codecogs.com/svg.latex?\inline&space;75).
2. Student ![equation](https://latex.codecogs.com/svg.latex?\inline&space;2) received a ![equation](https://latex.codecogs.com/svg.latex?\inline&space;67), and the next multiple of ![equation](https://latex.codecogs.com/svg.latex?\inline&space;5) from ![equation](https://latex.codecogs.com/svg.latex?\inline&space;67) is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;70). Since ![equation](https://latex.codecogs.com/svg.latex?\inline&space;70&space;-&space;67&space;=&space;3), the grade will not be modified and the student's final grade is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;67).
3. Student ![equation](https://latex.codecogs.com/svg.latex?\inline&space;3) received a ![equation](https://latex.codecogs.com/svg.latex?\inline&space;38), and the next multiple of ![equation](https://latex.codecogs.com/svg.latex?\inline&space;5) from ![equation](https://latex.codecogs.com/svg.latex?\inline&space;38) is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;40). Since ![equation](https://latex.codecogs.com/svg.latex?\inline&space;40&space;-&space;38&space;<&space;3), the student's grade will be rounded to ![equation](https://latex.codecogs.com/svg.latex?\inline&space;40).
4. Student ![equation](https://latex.codecogs.com/svg.latex?\inline&space;4) received a grade below ![equation](https://latex.codecogs.com/svg.latex?\inline&space;38), so the grade will not be modified and the student's final grade is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;33).
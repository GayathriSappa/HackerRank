Samantha was tasked with calculating the average monthly salaries for all employees in the __EMPLOYEES__ table, but did not realize her keyboard's ![equation](https://latex.codecogs.com/svg.latex?\inline&space;0) key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeroes removed), and the actual average salary.

Write a query calculating the amount of error (i.e.: ![equation](https://latex.codecogs.com/svg.latex?\inline&space;actual&space;-&space;miscalculated) average monthly salaries), and round it up to the next integer.

__Input Format__

The __EMPLOYEES__ table is described as follows:

![](https://github.com/avtomato/HackerRank/blob/master/SQL/img/1443817108-adc2235c81-1.png)

__Note:__ Salary is measured in dollars per month and its value is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;<&space;10^5).

__Sample Input__

![](https://github.com/avtomato/HackerRank/blob/master/SQL/img/1443817161-299cc6eb7f-2.png)

__Sample Output__
```commandline
2061
```
__Explanation__

The table below shows the salaries without zeroes as they were entered by Samantha:

![](https://github.com/avtomato/HackerRank/blob/master/SQL/img/1443817229-eb00d44a3b-3.png)

Samantha computes an average salary of ![equation](https://latex.codecogs.com/svg.latex?\inline&space;98,00). The actual average salary is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;2159,00).

The resulting error between the two calculations is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;2159.00&space;-&space;98.00&space;=&space;2061.00) which, when rounded to the next integer, is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;2061).

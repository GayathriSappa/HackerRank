We define an employee's total earnings to be their monthly ![equation](https://latex.codecogs.com/svg.latex?\inline&space;salary&space;\times&space;months) worked, and the maximum total earnings to be the maximum total earnings for any employee in the __Employee__ table. Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. Then print these values as ![equation](https://latex.codecogs.com/svg.latex?\inline&space;2) space-separated integers.

__Input Format__

The __Employee__ table containing employee data for a company is described as follows:

![](https://github.com/avtomato/HackerRank/blob/master/SQL/img/1458557872-4396838885-ScreenShot2016-03-21at4.27.13PM.png)

where employee_id is an employee's ID number, name is their name, months is the total number of months they've been working for the company, and salary is the their monthly salary.

Sample Input

![](https://github.com/avtomato/HackerRank/blob/master/SQL/img/1458559098-23bf583125-ScreenShot2016-03-21at4.32.59PM.png)

Sample Output
```commandline
69952 1
```
__Explanation__

The table and earnings data is depicted in the following diagram:
 
 ![](https://github.com/avtomato/HackerRank/blob/master/SQL/img/1458559218-9f37585c7a-ScreenShot2016-03-21at4.49.23PM.png)

The maximum earnings value is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;69952). The only employee with earnings ![equation](https://latex.codecogs.com/svg.latex?\inline&space;=&space;69952) is Kimberly, so we print the maximum earnings value (![equation](https://latex.codecogs.com/svg.latex?\inline&space;69952)) and a count of the number of employees who have earned ![equation](https://latex.codecogs.com/svg.latex?\inline&space;\$69952) (which is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1)) as two space-separated values.

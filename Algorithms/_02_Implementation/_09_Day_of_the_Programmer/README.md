Marie invented a [Time Machine](https://en.wikipedia.org/wiki/Time_machine) and wants to test it by time-traveling to visit Russia on the [Day of the Programmer](https://en.wikipedia.org/wiki/Day_of_the_Programmer) (the ![equation](https://latex.codecogs.com/svg.latex?\inline&space;256^{th}) day of the year) during a year in the inclusive range from ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1700) to ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2700).

From ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1700) to ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1917), Russia's official calendar was the [Julian calendar](https://en.wikipedia.org/wiki/Julian_calendar); since ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1919) they used the [Gregorian calendar](https://en.wikipedia.org/wiki/Gregorian_calendar) system. The transition from the Julian to Gregorian calendar system occurred in ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1918), when the next day after January ![equation](https://latex.codecogs.com/svg.latex?\inline&space;31^{st}) was February ![equation](https://latex.codecogs.com/svg.latex?\inline&space;14^{th}). This means that in ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1918), February ![equation](https://latex.codecogs.com/svg.latex?\inline&space;14^{th}) was the ![equation](https://latex.codecogs.com/svg.latex?\inline&space;32^{nd}) day of the year in Russia.

In both calendar systems, February is the only month with a variable amount of days; it has ![equation](http://latex.codecogs.com/svg.latex?\inline&space;29) days during a leap year, and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;28) days during all other years. In the Julian calendar, leap years are divisible by ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4); in the Gregorian calendar, leap years are either of the following:

* Divisible by ![equation](http://latex.codecogs.com/svg.latex?\inline&space;400).
* Divisible by ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4) and not divisible by ![equation](http://latex.codecogs.com/svg.latex?\inline&space;100).

Given a year, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;y), find the date of the ![equation](https://latex.codecogs.com/svg.latex?\inline&space;256^{th}) day of that year according to the official Russian calendar during that year. Then print it in the format dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit month, and yyyy is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;y).

__Input Format__

A single integer denoting year ![equation](http://latex.codecogs.com/svg.latex?\inline&space;y).

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1700&space;\le&space;y&space;\le&space;2700)

__Output Format__

Print the full date of Day of the Programmer during year ![equation](http://latex.codecogs.com/svg.latex?\inline&space;y) in the format dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit month, and yyyy is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;y).

__Sample Input 0__
```commandline
2017
```
__Sample Output 0__
```commandline
13.09.2017
```
__Explanation 0__

In the year ![equation](https://latex.codecogs.com/svg.latex?\inline&space;y&space;=&space;2017), January has ![equation](http://latex.codecogs.com/svg.latex?\inline&space;31) days, February has ![equation](http://latex.codecogs.com/svg.latex?\inline&space;28) days, March has ![equation](http://latex.codecogs.com/svg.latex?\inline&space;31) days, April has ![equation](http://latex.codecogs.com/svg.latex?\inline&space;30) days, May has ![equation](http://latex.codecogs.com/svg.latex?\inline&space;31) days, June has ![equation](http://latex.codecogs.com/svg.latex?\inline&space;30) days, July has ![equation](http://latex.codecogs.com/svg.latex?\inline&space;31) days, and August has ![equation](http://latex.codecogs.com/svg.latex?\inline&space;31) days. When we sum the total number of days in the first eight months, we get ![equation](https://latex.codecogs.com/svg.latex?\inline&space;31&space;&plus;&space;28&space;&plus;&space;31&space;&plus;&space;30&space;&plus;&space;31&space;&plus;&space;30&space;&plus;&space;31&space;&plus;&space;31&space;=&space;243). Day of the Programmer is the ![equation](https://latex.codecogs.com/svg.latex?\inline&space;256^{th}) day, so then calculate ![equation](https://latex.codecogs.com/svg.latex?\inline&space;256&space;-&space;243&space;=&space;13) to determine that it falls on day ![equation](http://latex.codecogs.com/svg.latex?\inline&space;13) of the ![equation](https://latex.codecogs.com/svg.latex?\inline&space;9^{th}) month (September). We then print the full date in the specified format, which is 13.09.2017.

__Sample Input 1__
```commandline
2016
```
__Sample Output 1__
```commandline
12.09.2016
```
__Explanation 1__

Year ![equation](https://latex.codecogs.com/svg.latex?\inline&space;y&space;=&space;2016) is a leap year, so February has ![equation](http://latex.codecogs.com/svg.latex?\inline&space;29) days but all the other months have the same number of days as in ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2017). When we sum the total number of days in the first eight months, we get ![equation](https://latex.codecogs.com/svg.latex?\inline&space;31&space;&plus;&space;29&space;&plus;&space;31&space;&plus;&space;30&space;&plus;&space;31&space;&plus;&space;30&space;&plus;&space;31&space;&plus;&space;31&space;=&space;244). Day of the Programmer is the ![equation](https://latex.codecogs.com/svg.latex?\inline&space;256^{th}) day, so then calculate ![equation](https://latex.codecogs.com/svg.latex?\inline&space;256&space;-&space;244&space;=&space;12) to determine that it falls on day ![equation](http://latex.codecogs.com/svg.latex?\inline&space;12) of the ![equation](https://latex.codecogs.com/svg.latex?\inline&space;9^{th}) month (September). We then print the full date in the specified format, which is 12.09.2016.
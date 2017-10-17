Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

1. If the book is returned on or before the expected return date, no fine will be charged (i.e.: ![equation](https://latex.codecogs.com/svg.latex?\inline&space;fine&space;=&space;0)).
2. If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, ![equation](https://latex.codecogs.com/svg.latex?\inline&space;fine&space;=&space;15\&space;Hackos\&space;(the\&space;number\&space;of\&space;days\&space;late)).
3. If the book is returned after the expected return month but still within the same calendar year as the expected return date, the ![equation](https://latex.codecogs.com/svg.latex?\inline&space;fine&space;=&space;500\&space;Hackos\&space;(the\&space;number\&space;of\&space;months\&space;late)).
4. If the book is returned after the calendar year in which it was expected, there is a fixed fine of ![equation](https://latex.codecogs.com/svg.latex?\inline&space;10000\&space;Hackos).

__Input Format__

The first line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3) space-separated integers denoting the respective ![equation](http://latex.codecogs.com/svg.latex?\inline&space;day), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;month), and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;year) on which the book was actually returned.<br> 
The second line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3) space-separated integers denoting the respective ![equation](http://latex.codecogs.com/svg.latex?\inline&space;day), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;month), and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;year) on which the book was expected to be returned (due date).

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\leq&space;D&space;\leq&space;31)
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\leq&space;M&space;\leq&space;12)
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\leq&space;Y&space;\leq&space;3000)
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;It\&space;is\&space;guaranteed\&space;that\&space;the\&space;dates\&space;will\&space;be\&space;valid\&space;Gregorian\&space;calendar\&space;dates)

__Output Format__

Print a single integer denoting the library fine for the book received as input.

__Sample Input__
```commandline
9 6 2015
6 6 2015
```
Sample Output
```commandline
45
```
__Explanation__

Given the following return dates:<br> 
Actual: ![equation](https://latex.codecogs.com/svg.latex?\inline&space;D_a&space;=&space;9,&space;M_a&space;=&space;6,&space;Y_a&space;=&space;2015)  
Expected: ![equation](https://latex.codecogs.com/svg.latex?\inline&space;D_e&space;=&space;6,&space;M_e&space;=&space;6,&space;Y_e&space;=&space;2015)

Because ![equation](https://latex.codecogs.com/svg.latex?\inline&space;Y_e&space;\equiv&space;Y_a), we know it is less than a year late.<br> 
Because ![equation](https://latex.codecogs.com/svg.latex?\inline&space;M_e&space;\equiv&space;M_a), we know it's less than a month late.<br> 
Because ![equation](https://latex.codecogs.com/svg.latex?\inline&space;D_e&space;<&space;D_a), we know that it was returned late (but still within the same month and year).

Per the library's fee structure, we know that our fine will be ![equation](https://latex.codecogs.com/svg.latex?\inline&space;15\&space;Hackos&space;\times&space;(\&hash;\&space;dates\&space;late)). We then print the result of ![equation](https://latex.codecogs.com/svg.latex?\inline&space;15&space;\times&space;(D_a&space;-&space;D_e)&space;=&space;15&space;\times&space;(9&space;-&space;6)&space;=&space;45) as our output.
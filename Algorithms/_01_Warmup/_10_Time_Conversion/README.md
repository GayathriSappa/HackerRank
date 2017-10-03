Given a time in [24-hour AM/PM format](https://en.wikipedia.org/wiki/12-hour_clock), convert it to military (![equation](http://latex.codecogs.com/svg.latex?\inline&space;24)-hour) time.

__Note:__ Midnight is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;12:00:00AM) on a -![equation](http://latex.codecogs.com/svg.latex?\inline&space;12)hour clock, and ![equation](https://latex.codecogs.com/svg.latex?\inline&space;00:00:00) on a ![equation](http://latex.codecogs.com/svg.latex?\inline&space;24)-hour clock. Noon is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;12:00:00PM) on a ![equation](http://latex.codecogs.com/svg.latex?\inline&space;12)-hour clock, and ![equation](https://latex.codecogs.com/svg.latex?\inline&space;12:00:00) on a ![equation](http://latex.codecogs.com/svg.latex?\inline&space;24)-hour clock.

__Input Format__<br>
A single string containing a time in ![equation](http://latex.codecogs.com/svg.latex?\inline&space;12)-hour clock format (i.e.: ![equation](https://latex.codecogs.com/svg.latex?\inline&space;hh:mm:ssAM) or ![equation](https://latex.codecogs.com/svg.latex?\inline&space;hh:mm:ssPM)), where ![equation](https://latex.codecogs.com/svg.latex?\inline&space;01&space;\le&space;hh&space;\le&space;12) and ![equation](https://latex.codecogs.com/svg.latex?\inline&space;00&space;\le&space;mm,ss&space;\le&space;59).

__Output Format__
Convert and print the given time in ![equation](http://latex.codecogs.com/svg.latex?\inline&space;24)-hour format, where ![equation](https://latex.codecogs.com/svg.latex?\inline&space;0&space;\le&space;hh&space;\le&space;23).

__Sample Input__
```commandline
07:05:45PM
```
__Sample Output__
```commandline
19:05:45
```

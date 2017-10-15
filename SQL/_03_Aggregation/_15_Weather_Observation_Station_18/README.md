Consider ![equation](https://latex.codecogs.com/svg.latex?\inline&space;P_1(a,b)) and ![equation](https://latex.codecogs.com/svg.latex?\inline&space;P_2(c,d)) to be two points on a 2D plane.

* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;a) happens to equal the minimum value in Northern Latitude (LAT_N in __STATION__).
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;b) happens to equal the minimum value in Western Longitude (LONG_W in __STATION__).
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;c) happens to equal the maximum value in Northern Latitude (LAT_N in __STATION__).
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;d) happens to equal the maximum value in Western Longitude (LONG_W in __STATION__).

Query the [Manhattan Distance](https://xlinux.nist.gov/dads/HTML/manhattanDistance.html) between points ![equation](https://latex.codecogs.com/svg.latex?\inline&space;P_1) and ![equation](https://latex.codecogs.com/svg.latex?\inline&space;P_2) and round it to a scale of ![equation](https://latex.codecogs.com/svg.latex?\inline&space;4) decimal places.

__Input Format__

The __STATION__ table is described as follows:

![](https://github.com/avtomato/HackerRank/blob/master/SQL/img/1449345840-5f0a551030-Station.jpg)

where LAT_N is the northern latitude and LONG_W is the western longitude.
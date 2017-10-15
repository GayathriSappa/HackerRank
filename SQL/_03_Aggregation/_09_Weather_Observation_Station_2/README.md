Query the following two values from the __STATION__ table:

1. The sum of all values in LAT_N rounded to a scale of ![equation](https://latex.codecogs.com/svg.latex?\inline&space;2) decimal places.
2. The sum of all values in LONG_W rounded to a scale of ![equation](https://latex.codecogs.com/svg.latex?\inline&space;2) decimal places.

__Input Format__

The __STATION__ table is described as follows:

![](https://github.com/avtomato/HackerRank/blob/master/SQL/img/1449345840-5f0a551030-Station.jpg)

where LAT_N is the northern latitude and LONG_W is the western longitude.

__Output Format__

Your results must be in the form:
```commandline
lat lon
```
where ![equation](https://latex.codecogs.com/svg.latex?\inline&space;lat) is the sum of all values in LAT_N and ![equation](https://latex.codecogs.com/svg.latex?\inline&space;lon) is the sum of all values in LONG_W. Both results must be rounded to a scale of ![equation](https://latex.codecogs.com/svg.latex?\inline&space;2) decimal places.
Query the two cities in __STATION__ with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

__Input Format__

The __STATION__ table is described as follows:

![](https://github.com/avtomato/HackerRank/blob/master/SQL/img/1449345840-5f0a551030-Station.jpg)

where LAT_N is the northern latitude and LONG_W is the western longitude.

__Sample Input__

Let's say that CITY only has four entries: DEF, ABC, PQRS and WXY

__Sample Output__
```commandline
ABC 3
PQRS 4
```
__Explanation__

When ordered alphabetically, the CITY names are listed as ABC, DEF, PQRS, and WXY, with the respective lengths ![equation](https://latex.codecogs.com/svg.latex?\inline&space;3,&space;3,&space;4,) and ![equation](https://latex.codecogs.com/svg.latex?\inline&space;3). The longest-named city is obviously PQRS, but there are ![equation](https://latex.codecogs.com/svg.latex?\inline&space;3) options for shortest-named city; we choose ABC, because it comes first alphabetically.

__Note<br> 
You can write two separate queries to get the desired output. It need not be a single query.__
Two cats named ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B) are standing at integral points on the x-axis. Cat ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) is standing at point ![equation](http://latex.codecogs.com/svg.latex?\inline&space;x) and cat ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B) is standing at point ![equation](http://latex.codecogs.com/svg.latex?\inline&space;y). Both cats run at the same speed, and they want to catch a mouse named ![equation](http://latex.codecogs.com/svg.latex?\inline&space;C) that's hiding at integral point ![equation](http://latex.codecogs.com/svg.latex?\inline&space;z) on the x-axis. Can you determine who will catch the mouse?

You are given ![equation](http://latex.codecogs.com/svg.latex?\inline&space;q) queries in the form of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;x), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;y), and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;z). For each query, print the appropriate answer on a new line:

* If cat ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) catches the mouse first, print Cat A.
* If cat ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B) catches the mouse first, print Cat B.
* If both cats reach the mouse at the same time, print Mouse C as the two cats fight and mouse escapes.

__Input Format__

The first line contains a single integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;q), denoting the number of queries. 
Each of the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;q) subsequent lines contains three space-separated integers describing the respective values of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;x) (cat ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A)'s location), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;y) (cat ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B)'s location), and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;z) (mouse ![equation](http://latex.codecogs.com/svg.latex?\inline&space;C)'s location).

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\le&space;q&space;\le&space;100)
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\le&space;x,y,z&space;\le&space;100)

__Output Format__

On a new line for each query, print Cat A if cat ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) catches the mouse first, Cat B if cat ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B) catches the mouse first, or Mouse C if the mouse escapes.

__Sample Input 0__
```commandline
3
1 2 3
1 3 2
2 1 3
```
__Sample Output 0__
```commandline
Cat B
Mouse C
Cat A
```
__Explanation 0__

Query 0: The positions of the cats and mouse are shown below: 

![](https://github.com/avtomato/HackerRank/blob/master/Algorithms/img/1480434477-7418fccf34-cat.png)

Cat ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B) will catch the mouse first, so we print Cat B on a new line.

Query 1: In this query, cats ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B) reach mouse ![equation](http://latex.codecogs.com/svg.latex?\inline&space;C) at the exact same time: 

![](https://github.com/avtomato/HackerRank/blob/master/Algorithms/img/1480434557-601bef86ba-cat1.png)

Because the mouse escapes, we print Mouse C on a new line.
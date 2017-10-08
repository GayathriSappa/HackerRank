Sam's house has an apple tree and an orange tree that yield an abundance of fruit. In the diagram below, the red region denotes his house, where ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s) is the start point and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;t) is the end point. The apple tree is to the left of his house, and the orange tree is to its right. You can assume the trees are located on a single point, where the apple tree is at point ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a) and the orange tree is at point ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b).

![](https://github.com/avtomato/HackerRank/blob/master/Algorithms/img/1474218925-f2a791d52c-Appleandorange2.png)

When a fruit falls from its tree, it lands ![equation](http://latex.codecogs.com/svg.latex?\inline&space;d) units of distance from its tree of origin along the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;x)-axis. A negative value of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;d) means the fruit fell ![equation](http://latex.codecogs.com/svg.latex?\inline&space;d) units to the tree's left, and a positive value of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;d) means it falls ![equation](http://latex.codecogs.com/svg.latex?\inline&space;d) units to the tree's right.

Given the value of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;d) for ![equation](http://latex.codecogs.com/svg.latex?\inline&space;m) apples and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) oranges, can you determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range ![equation](http://latex.codecogs.com/svg.latex?\inline&space;[s,t])? Print the number of apples that fall on Sam's house as your first line of output, then print the number of oranges that fall on Sam's house as your second line of output.

__Input Format__

The first line contains two space-separated integers denoting the respective values of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;t).<br> 
The second line contains two space-separated integers denoting the respective values of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b).<br> 
The third line contains two space-separated integers denoting the respective values of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;m) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n).<br> 
The fourth line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;m) space-separated integers denoting the respective distances that each apple falls from point ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a).<br> 
The fifth line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) space-separated integers denoting the respective distances that each orange falls from point ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b).

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\le&space;s,t,a,b,m,n&space;\le&space;10^5)
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;-10^5&space;\le&space;d&space;\le&space;10^5)
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;a&space;<&space;s&space;<&space;t&space;<&space;b)

__Output Format__

Print two lines of output:
* On the first line, print the number of apples that fall on Sam's house.
* On the second line, print the number of oranges that fall on Sam's house.

__Sample Input 0__
```commandline
7 11
5 15
3 2
-2 2 1
5 -6
```
__Sample Output 0__
```commandline
1
1
```
__Explanation 0__

The first apple falls at position ![equation](https://latex.codecogs.com/svg.latex?\inline&space;5&space;-&space;2&space;=&space;3).<br> 
The second apple falls at position ![equation](https://latex.codecogs.com/svg.latex?\inline&space;5&space;+&space;2&space;=&space;7).<br> 
The third apple falls at position ![equation](https://latex.codecogs.com/svg.latex?\inline&space;5&space;+&space;1&space;=&space;6).<br> 
The first orange falls at position ![equation](https://latex.codecogs.com/svg.latex?\inline&space;15&space;+&space;5&space;=&space;20).<br> 
The second orange falls at position ![equation](https://latex.codecogs.com/svg.latex?\inline&space;15&space;-&space;6&space;=&space;9).<br> 
Only one fruit (the second apple) falls within the region between ![equation](http://latex.codecogs.com/svg.latex?\inline&space;7) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;11), so we print ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1) as our first line of output.<br> 
Only the second orange falls within the region between ![equation](http://latex.codecogs.com/svg.latex?\inline&space;7) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;11), so we print ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1) as our second line of output.
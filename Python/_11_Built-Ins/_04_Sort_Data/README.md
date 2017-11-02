You are given data in a tabular format. The data contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) rows, and each row contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M) space separated elements.

You can imagine the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M) items to be different attributes, (like height, weight, energy, etc.) and each of the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) rows as an instance or a sample.

Your task is to sort the table based on the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;K^{th}) attribute and print the final resulting table. Note that ![equation](http://latex.codecogs.com/svg.latex?\inline&space;K) is indexed from ![equation](http://latex.codecogs.com/svg.latex?\inline&space;0) to ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20M%20-%201).

__Note:__ If two attributes are the same for different rows, print the row that appeared first in the input.

__Input Format__

The first line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M) separated by a space. <br>
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines each contain ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M) elements. <br>
The last line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;K).

__Constraints__

 ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20N%2C%20M%20%5Cleq%201000) <br>
 ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%5Cleq%20K%20%3C%20M) <br> 
Each element ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20%5Cleq%201000)

__Output Format__

Print the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

__Sample Input__
```commandline
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
```
__Sample Output__
```commandline
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
```
__Explanation__

The table is sorted on the second attribute shown as ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20K%20%3D%201) because it's ![equation](http://latex.codecogs.com/svg.latex?\inline&space;0)-indexed.
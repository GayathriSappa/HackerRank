You are given a function ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20f%28X%29%20%3D%20X%5E2). You are also given ![equation](http://latex.codecogs.com/svg.latex?\inline&space;K) lists. The ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i^{th}) list consists of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) elements.

You have to pick one element from each list so that the value from the equation below is maximized: 

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20S%20%3D%20%28f%28X_1%29%20&plus;%20f%28X_2%29%20&plus;%20...%20&plus;%20f%28X_k%29%29)%![equation](http://latex.codecogs.com/svg.latex?\inline&space;M)

![equation](http://latex.codecogs.com/svg.latex?\inline&space;X_i) denotes the element picked from the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i^{th}) list . Find the maximized value ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S_{max}) obtained.

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20%5C%25) denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

__Input Format__

The first line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) space separated integers ![equation](http://latex.codecogs.com/svg.latex?\inline&space;K) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;M). <br> 
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;K) lines each contains an integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N_i) followed by ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N_i) space separated integers denoting the elements in the list.

__Constraints__

 ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20K%20%5Cleq%207)<br>
 ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20M%20%5Cleq%201000)<br>
 ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20N_i%20%5Cleq%207)<br>
 ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20Magnitude%5C%20of%5C%20elements%5C%20in%5C%20lists%20%5Cleq%2010%5E9)

__Output Format__

Output a single integer denoting the value ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S_{max}).

__Sample Input__
```commandline
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10
``` 
__Sample Output__
```commandline
206
```
__Explanation__

Picking ![equation](http://latex.codecogs.com/svg.latex?\inline&space;5) from the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1^{st}) list, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;9) from the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2^{nd}) list and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;10) from the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3^{rd}) list gives the maximum ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S) value equal to ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20%285%5E2%20&plus;%209%5E2%20&plus;%2010%5E2%29)%![equation](http://latex.codecogs.com/svg.latex?\inline&space;1000) = ![equation](http://latex.codecogs.com/svg.latex?\inline&space;206).
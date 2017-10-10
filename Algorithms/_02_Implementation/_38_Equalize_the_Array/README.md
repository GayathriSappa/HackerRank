Karl has an array of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) integers defined as ![equation](https://latex.codecogs.com/svg.latex?\inline&space;A&space;=&space;a_0,&space;a_1,&space;...,&space;a_{n-1}). In one operation, he can delete any element from the array.

Karl wants all the elements of the array to be equal to one another. To do this, he must delete zero or more elements from the array. Find and print the minimum number of deletion operations Karl must perform so that all the array's elements are equal.

__Input Format__

The first line contains an integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n), denoting the number of elements in array ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A).<br> 
The next line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) space-separated integers where element ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i) corresponds to array element ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a_i) (![equation](https://latex.codecogs.com/svg.latex?\inline&space;0&space;\leq&space;i&space;<&space;n)).

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\le&space;n&space;\le&space;100)
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\le&space;a_i&space;\le&space;100)

__Output Format__

Print a single integer denoting the minimum number of elements Karl must delete for all elements in the array to be equal.

__Sample Input__
```commandline
5
3 3 2 1 3
```
__Sample Output__
```commandline
2
```  
__Explanation__

Array ![equation](https://latex.codecogs.com/svg.latex?\inline&space;A&space;=&space;[3,&space;3,&space;2,&space;1,&space;3]). If we delete ![equation](https://latex.codecogs.com/svg.latex?\inline&space;a_2&space;=&space;2) and ![equation](https://latex.codecogs.com/svg.latex?\inline&space;a_3&space;=&space;1), all of the elements in the resulting array, ![equation](https://latex.codecogs.com/svg.latex?\inline&space;\AA&space;=&space;[3,&space;3,&space;3]), will be equal. Deleting these ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) elements is minimal because our only other options would be to delete ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4) elements to get an array of either ![equation](http://latex.codecogs.com/svg.latex?\inline&space;[1]) or ![equation](http://latex.codecogs.com/svg.latex?\inline&space;[2]). Thus, we print ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) on a new line, as that is the minimum number of deletions resulting in an array where all elements are equal.
A flock of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) birds is flying across the continent. Each bird has a type, and the different types are designated by the ID numbers ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4), and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;5).

Given an array of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) integers where each integer describes the type of a bird in the flock, find and print the type number of the most common bird. If two or more types of birds are equally common, choose the type with the smallest ID number.

__Input Format__

The first line contains an integer denoting ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) (the number of birds).<br> 
The second line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) space-separated integers describing the respective type numbers of each bird in the flock.

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;5\leq&space;n&space;\leq&space;2&space;\times&space;10^5)
* It is guaranteed that each type is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4), or ![equation](http://latex.codecogs.com/svg.latex?\inline&space;5).
__Output Format__

Print the type number of the most common bird; if two or more types of birds are equally common, choose the type with the smallest ID number.

Sample Input 0
```commandline
6
1 4 4 4 5 3
```
__Sample Output 0__
```commandline
4
```
__Explanation 0__

The different types of birds occur in the following frequencies:

* Type ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1): ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1) bird
* Type ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2): ![equation](http://latex.codecogs.com/svg.latex?\inline&space;0) birds
* Type ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3): ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1) bird
* Type ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4): ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3) birds
* Type ![equation](http://latex.codecogs.com/svg.latex?\inline&space;5): ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1) bird

The type number that occurs at the highest frequency is type ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4), so we print ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4) as our answer.
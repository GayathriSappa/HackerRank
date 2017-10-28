You are given a set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) other sets.<br> 
Your job is to find whether set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) is a strict superset of each of the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) sets.

Print True, if ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) is a strict superset of each of the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

__Example__

Set ![equation](https://latex.codecogs.com/svg.latex?\inline&space;([1,&space;3,&space;4])) is a strict superset of set ![equation](https://latex.codecogs.com/svg.latex?\inline&space;([1,&space;3])) .<br> 
Set ![equation](https://latex.codecogs.com/svg.latex?\inline&space;([1,&space;3,&space;4])) is not a strict superset of set ![equation](https://latex.codecogs.com/svg.latex?\inline&space;([1,&space;3,&space;4])) .<br> 
Set ![equation](https://latex.codecogs.com/svg.latex?\inline&space;([1,&space;3,&space;4])) is not a strict superset of set ![equation](https://latex.codecogs.com/svg.latex?\inline&space;([1,&space;3,&space;5])) .

__Input Format__

The first line contains the space separated elements of set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A).<br> 
The second line contains integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n), the number of other sets.<br> 
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) lines contains the space separated elements of the other sets.

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20len%28set%28A%29%29%20%3C%20501)
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;0&space;<&space;N&space;<&space;21)
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;0&space;<&space;len(otherSets)&space;<&space;101)

__Output Format__

Print True if set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) is a strict superset of all other ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) sets. Otherwise, print False.

__Sample Input 0__
```commandline
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
```
__Sample Output 0__
```commandline
False
```
__Explanation 0__

Set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) is the strict superset of the set ![equation](https://latex.codecogs.com/svg.latex?\inline&space;([1,&space;2,&space;3,&space;4,&space;5)) but not of the set ![equation](https://latex.codecogs.com/svg.latex?\inline&space;([100,&space;11,&space;12])) because ![equation](http://latex.codecogs.com/svg.latex?\inline&space;100) is not in set ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A).<br> 
Hence, the output is False.
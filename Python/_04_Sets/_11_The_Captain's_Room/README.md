Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

One fine day, a finite number of tourists come to stay at the hotel.<br> 
The tourists consist of:<br>
→ A Captain.<br>
→ An unknown group of families consisting of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;K) members per group where ![equation](http://latex.codecogs.com/svg.latex?\inline&space;K) ≠ ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1).

The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear ![equation](http://latex.codecogs.com/svg.latex?\inline&space;K) times per group except for the Captain's room.

Mr. Anant needs you to help him find the Captain's room number.<br> 
The total number of tourists or the total number of groups of families is not known to you.<br> 
You only know the value of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;K) and the room number list.

__Input Format__

The first line consists of an integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;K), the size of each group.<br>
The second line contains the unordered elements of the room number list.


__Constraints__

![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;<&space;K&space;<&space;1000)

__Output Format__

Output the Captain's room number.

__Sample Input__
```commandline
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
```
__Sample Output__
```commandline
8
```
__Explanation__

The list of room numbers contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;31) elements. Since ![equation](http://latex.codecogs.com/svg.latex?\inline&space;K) is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;5), there must be ![equation](http://latex.codecogs.com/svg.latex?\inline&space;6) groups of families. In the given list, all of the numbers repeat ![equation](http://latex.codecogs.com/svg.latex?\inline&space;5) times except for room number ![equation](http://latex.codecogs.com/svg.latex?\inline&space;8).<br> 
Hence, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;8) is the Captain's room number.
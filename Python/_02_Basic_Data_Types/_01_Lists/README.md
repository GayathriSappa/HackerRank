Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;e) at position ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i).
2. print: Print the list.
3. remove e: Delete the first occurrence of integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;e).
4. append e: Insert integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;e) at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.

Initialize your list and read in the value of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) followed by ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) lines of commands where each command will be of the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;7) types listed above. Iterate through each command in order and perform the corresponding operation on your list.

__Input Format__

The first line contains an integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n), denoting the number of commands.<br> 
Each line ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i) of the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) subsequent lines contains one of the commands described above.

__Constraints__
* The elements added to the list must be integers.

__Output Format__

For each command of type print, print the list on a new line.

__Sample Input__
```commandline
12
insert 0 5
insert 1 10
insert 0 6
print 
remove 6
append 9
append 1
sort 
print
pop
reverse
print
```
__Sample Output__
```commandline
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
```
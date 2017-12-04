In Insertion Sort Part 1, you sorted one element into an array. Using the same approach repeatedly, can you sort an entire unsorted array?

Guideline: You already can place an element into a sorted array. How can you use that code to build up a sorted array, one element at a time? Note that in the first step, when you consider an array with just the first element - that is already "sorted" since there's nothing to its left that is smaller.

In this challenge, don't print every time you move an element. Instead, print the array after each iteration of the insertion-sort, i.e., whenever the next element is placed at its correct position.

Since the array composed of just the first element is already "sorted", begin printing from the second element and on.

__Input Format__<br> 
There will be two lines of input:
* ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s) - the size of the array
* ![equation](http://latex.codecogs.com/svg.latex?\inline&space;ar) - a list of numbers that makes up the array

__Output Format__<br> 
On each line, output the entire array at every iteration.

__Constraints__ 
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\leq&space;s&space;\leq&space;1000)
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;-10000&space;\leq&space;x&space;\leq&space;10000,&space;x&space;\in&space;ar)

__Sample Input__
```commandline
6
1 4 3 5 6 2
```
__Sample Output__
```commandline
1 4 3 5 6 2 
1 3 4 5 6 2 
1 3 4 5 6 2 
1 3 4 5 6 2 
1 2 3 4 5 6
``` 
__Explanation__ 
Insertion Sort checks ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4) first and doesn't need to move it, so it just prints out the array. Next, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3) is inserted next to ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1), and the array is printed out. This continues one element at a time until the entire array is sorted.

__Task__<br> 
The method __insertionSort__ takes in one parameter: ![equation](http://latex.codecogs.com/svg.latex?\inline&space;ar), an unsorted array. Use an Insertion Sort Algorithm to sort the entire array.
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

__Input Format__<br>
A single line of five space-separated integers.

__Constraints__
* Each integer is in the inclusive range ![equation](https://latex.codecogs.com/svg.latex?\inline&space;[1,&space;10^9]).

__Output Format__<br>
Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than 32 bit integer.)

__Sample Input__
```commandline
1 2 3 4 5
```
__Sample Output__
```commandline
10 14
```
__Explanation__

Our initial numbers are ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4), and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;5). We can calculate the following sums using four of the five integers:

1. If we sum everything except ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1), our sum is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;2&space;&plus;&space;3&space;&plus;&space;4&space;&plus;&space;5&space;=&space;14).
2. If we sum everything except ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2), our sum is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;&plus;&space;3&space;&plus;&space;4&space;&plus;&space;5&space;=&space;13).
3. If we sum everything except ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3), our sum is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;&plus;&space;2&space;&plus;&space;4&space;&plus;&space;5&space;=&space;12).
4. If we sum everything except ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4), our sum is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;&plus;&space;2&space;&plus;&space;3&space;&plus;&space;5&space;=&space;11).
5. If we sum everything except ![equation](http://latex.codecogs.com/svg.latex?\inline&space;5), our sum is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;&plus;&space;2&space;&plus;&space;3&space;&plus;&space;4&space;=&space;10).

As you can see, the minimal sum is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;&plus;&space;2&space;&plus;&space;3&space;&plus;&space;4&space;=&space;10) and the maximal sum is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;2&space;&plus;&space;3&space;&plus;&space;4&space;&plus;&space;5&space;=&space;14). Thus, we print these minimal and maximal sums as two space-separated integers on a new line.

__Hints:__ Beware of integer overflow! Use 64-bit Integer.

Need help to get started? Try the [Solve Me First](https://www.hackerrank.com/challenges/solve-me-first) problem
We say that a string, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s), contains the word hackerrank if a [subsequence](https://en.wikipedia.org/wiki/Subsequence) of the characters in ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s) spell the word hackerrank. For example, haacckkerrannkk does contain hackerrank, but haacckkerannk does not (the characters all appear in the same order, but it's missing a second r).

More formally, let ![equation](https://latex.codecogs.com/svg.latex?\inline&space;p_0,&space;p_1,&space;...,&space;p_9) be the respective indices of h, a, c, k, e, r, r, a, n, k in string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s). If ![equation](https://latex.codecogs.com/svg.latex?\inline&space;p_0&space;<&space;p_1&space;<&space;p_2&space;<&space;...&space;<&space;p_9) is true, then ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s) contains hackerrank.

You must answer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;q) queries, where each query consists of a string, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s). For each query, print YES on a new line if ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s) contains hackerrank; otherwise, print NO instead.

__Input Format__

The first line contains an integer denoting ![equation](http://latex.codecogs.com/svg.latex?\inline&space;q) (the number of queries).<br> 
Each line of the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;q) subsequent lines contains a single string denoting ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s).

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;2&space;\le&space;q&space;\le&space;10^2)
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;10&space;\le&space;length(s)&space;\le&space;10^4)

__Output Format__

For each query, print YES on a new line if ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s_i) contains hackerrank; otherwise, print NO instead.

__Sample Input 0__
```commandline
2
hereiamstackerrank
hackerworld
```
__Sample Output 0__
```commandline
YES
NO
```
__Explanation 0__

We perform the following ![equation](https://latex.codecogs.com/svg.latex?\inline&space;q&space;=&space;2) queries:

 
1. ![equation](https://latex.codecogs.com/svg.latex?\inline&space;s&space;=&space;\mathbf{h}erei\mathbf{a}msta\mathbf{ckerrank})<br>The characters of hackerrank are bolded in the string above. Because the string contains all the characters in hackerrank in the same exact order as they appear in hackerrank, we print YES on a new line.<br>
2. ![equation](https://latex.codecogs.com/svg.latex?\inline&space;s&space;=&space;\mathbf{hacker}wo\mathbf{r}ld) does not contain the last three characters of hackerrank, so we print NO on a new line.
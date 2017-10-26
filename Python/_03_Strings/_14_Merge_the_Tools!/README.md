Consider the following:

* A string, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s), of length  where .
* An integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;k), where ![equation](http://latex.codecogs.com/svg.latex?\inline&space;k) is a factor of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n).

We can split ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s) into ![equation](https://latex.codecogs.com/svg.latex?\inline&space;\frac{n}{k}) subsegments where each subsegment, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;t_i), consists of a contiguous block of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;k) characters in ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s). Then, use each ![equation](http://latex.codecogs.com/svg.latex?\inline&space;t_i) to create string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;u_i) such that:

* The characters in ![equation](http://latex.codecogs.com/svg.latex?\inline&space;u_i) are a subsequence of the characters in ![equation](http://latex.codecogs.com/svg.latex?\inline&space;t_i).
* Any repeat occurrence of a character is removed from the string such that each character in ![equation](http://latex.codecogs.com/svg.latex?\inline&space;u_i) occurs exactly once. In other words, if the character at some index ![equation](http://latex.codecogs.com/svg.latex?\inline&space;j) in ![equation](http://latex.codecogs.com/svg.latex?\inline&space;t_i) occurs at a previous index ![equation](http://latex.codecogs.com/svg.latex?\inline&space;<j) in ![equation](http://latex.codecogs.com/svg.latex?\inline&space;t_i), then do not include the character in string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;u_i).

Given ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;k), print ![equation](https://latex.codecogs.com/svg.latex?\inline&space;\frac{n}{k}) lines where each line ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i) denotes string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;u_i).

__Input Format__

The first line contains a single string denoting ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s).<br> 
The second line contains an integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;k), denoting the length of each subsegment.

__Constraints__

* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\leq&space;n&space;\leq&space;10^4), where ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) is the length of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s) 
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\leq&space;k&space;\leq&space;n)
* It is guaranteed that ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) is a multiple of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;k).

__Output Format__

Print ![equation](https://latex.codecogs.com/svg.latex?\inline&space;\frac{n}{k}) lines where each line ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i) contains string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;u_i).

__Sample Input__
```commandline
AABCAAADA
3  
``` 
__Sample Output__
```commandline
AB
CA
AD
```
__Explanation__

String ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s) is split into ![equation](https://latex.codecogs.com/svg.latex?\inline&space;\frac{n}{k}&space;=&space;\frac{9}{3}&space;=&space;3) equal parts of length ![equation](https://latex.codecogs.com/svg.latex?\inline&space;k&space;=&space;3). We convert each ![equation](http://latex.codecogs.com/svg.latex?\inline&space;t_i) to ![equation](http://latex.codecogs.com/svg.latex?\inline&space;u_i) by removing any subsequent occurrences non-distinct characters in ![equation](http://latex.codecogs.com/svg.latex?\inline&space;t_i):
1. ![equation](https://latex.codecogs.com/svg.latex?\inline&space;t_0&space;=&space;\mathbf{"AAB"}&space;\rightarrow&space;u_0&space;=&space;\mathbf{"AB"})
2. ![equation](https://latex.codecogs.com/svg.latex?\inline&space;t_1&space;=&space;\mathbf{"CAA"}&space;\rightarrow&space;u_1&space;=&space;\mathbf{"CA"})
3. ![equation](https://latex.codecogs.com/svg.latex?\inline&space;t_2&space;=&space;\mathbf{"ADA"}&space;\rightarrow&space;u_2&space;=&space;\mathbf{"AD"})
 
We then print each ![equation](http://latex.codecogs.com/svg.latex?\inline&space;u_i) on a new line.
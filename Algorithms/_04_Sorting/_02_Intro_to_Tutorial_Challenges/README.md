__About Tutorial Challenges__<br> 
Many of the challenges on HackerRank are difficult and assume that you already know the relevant algorithms very well. These tutorial challenges are different. They break down algorithmic concepts into smaller challenges, so that you can learn the algorithm by solving the challenges.

These challenges are intended for those who know some programming and now want to learn some algorithms. You could be a student majoring in Computers, a self-taught programmer, or an experienced developer who wants an active algorithms review!

The first series of challenges covers sorting. The challenges are listed below:

__Tutorial Challenges - Sorting__

Insertion Sort challenges
* [Insertion Sort 1 - Inserting](https://www.hackerrank.com/challenges/insertionsort1)
* [Insertion Sort 2 - Sorting](https://www.hackerrank.com/challenges/insertionsort2)
* [Correctness and loop invariant](https://www.hackerrank.com/challenges/correctness-invariant)
* [Running Time of Algorithms](https://www.hackerrank.com/challenges/runningtime)

Quicksort challenges
* [Quicksort 1 - Partition](https://www.hackerrank.com/challenges/quicksort1)
* [Quicksort 2 - Sorting](https://www.hackerrank.com/challenges/quicksort2)
* [Quicksort In-place (advanced)](https://www.hackerrank.com/challenges/quicksort3)
* [Running time of Quicksort](https://www.hackerrank.com/challenges/quicksort4)

Counting sort challenges
* [Counting Sort 1 - Counting](https://www.hackerrank.com/challenges/countingsort1)
* [Counting Sort 2 - Simple sort](https://www.hackerrank.com/challenges/countingsort2)
* [Counting Sort 3 - Preparing](https://www.hackerrank.com/challenges/countingsort3)
* [Full Counting Sort (advanced)](https://www.hackerrank.com/challenges/countingsort4)

There will also be some challenges where you'll get to apply what you've learnt.

__About the Challenges__<br> 
The challenges will describe some topic and then ask you to code a solution. As you progress through the challenges, you will learn some important concepts in algorithms. In each challenge, you will receive input on [STDIN](http://en.wikipedia.org/wiki/Standard_streams#Standard_input_.28stdin.29) and you will need to print the correct output to STDOUT.

For many challenges, helper methods (like an array) will be provided for you to process the input into a useful format. You can use these methods to get started with your program, or you can write your own input methods if you want. Your code just needs to print the right output to each test case.

__Sample Challenge__<br> 
This is a simple challenge to get things started. Given a sorted array (![equation](http://latex.codecogs.com/svg.latex?\inline&space;ar)) and a number (![equation](http://latex.codecogs.com/svg.latex?\inline&space;V)), can you print the index location of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;V) in the array?

The next section describes the input format. You can often skip it, if you are using included methods.

__Input Format__<br> 
There will be three lines of input:
* ![equation](http://latex.codecogs.com/svg.latex?\inline&space;V) - the value that has to be searched.
* ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) - the size of the array.
* ![equation](http://latex.codecogs.com/svg.latex?\inline&space;ar) - ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) numbers that make up the array.

__Output Format__<br> 
Output the index of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;V) in the array.

The next section describes the constraints and ranges of the input. You should check this section to know the range of the input.

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\leq&space;n&space;\leq&space;1000)
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;-1000&space;\leq&space;V&space;\leq&space;1000,&space;V&space;\in&space;ar)
* It is guaranteed that ![equation](http://latex.codecogs.com/svg.latex?\inline&space;V) will occur in ![equation](http://latex.codecogs.com/svg.latex?\inline&space;ar) exactly once.

This "sample" shows the first input test case. It is often useful to go through the sample to understand a challenge.

__Sample Input__
```commandline
4
6
1 4 5 7 9 12
```
__Sample Output__
```commandline
1
```
__Explanation__<br> 
![equation](https://latex.codecogs.com/svg.latex?\inline&space;V&space;=&space;4). The value ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4) is the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2^{nd}) element in the array, but its index is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1) since array indices start from ![equation](http://latex.codecogs.com/svg.latex?\inline&space;0), so the answer is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1).
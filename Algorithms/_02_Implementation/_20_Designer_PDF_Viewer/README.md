When you select a contiguous block of text in a PDF viewer, the selection is highlighted with a blue rectangle. In a new kind of PDF viewer, the selection of each word is independent of the other words; this means that each rectangular selection area forms independently around each highlighted word. For example:

![](https://github.com/avtomato/HackerRank/blob/master/Algorithms/img/1471640108-6c01750b16-PDF-highighting.png)

In this type of PDF viewer, the width of the rectangular selection area is equal to the number of letters in the word times the width of a letter, and the height is the maximum height of any letter in the word.

Consider a word consisting of lowercase English alphabetic letters, where each letter is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1mm) wide. Given the height of each letter in millimeters (![equation](http://latex.codecogs.com/svg.latex?\inline&space;mm)), find the total area that will be highlighted by blue rectangle in ![equation](http://latex.codecogs.com/svg.latex?\inline&space;mm^2) when the given word is selected in our new PDF viewer.

__Input Format__

The first line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;26) space-separated integers describing the respective heights of each consecutive lowercase English letter (i.e., ![equation](https://latex.codecogs.com/svg.latex?\inline&space;h_a,&space;h_b,&space;h_c,&space;...,&space;h_y,&space;h_z)).<br> 
The second line contains a single word, consisting of lowercase English alphabetic letters.

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\leq&space;h_?&space;\leq&space;7), where ![equation](http://latex.codecogs.com/svg.latex?\inline&space;?) is an English lowercase letter.
* Word contains no more than ![equation](http://latex.codecogs.com/svg.latex?\inline&space;10) letters.

__Output Format__

Print a single integer denoting the area of highlighted rectangle when the given word is selected. The unit of measurement for this is square millimeters (![equation](http://latex.codecogs.com/svg.latex?\inline&space;mm^2)), but you must only print the integer.

__Sample Input 0__
```commandline
1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
abc
```
__Sample Output 0__
```commandline
9
```
__Explanation 0__

We are highlighting the word abc:

1. The tallest letter in abc is b, and ![equation](https://latex.codecogs.com/svg.latex?\inline&space;h_b&space;=&space;3). The selection area for this word is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;3&space;*&space;1mm&space;*&space;3mm&space;=&space;9mm^2).

__Note:__ Recall that the width of each character is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1mm).

__Sample Input 1__
```commandline
1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7
zaba
```
__Sample Output 1__
```commandline
28
```
__Explanation 1__

We are highlighting the word ![equation](http://latex.codecogs.com/svg.latex?\inline&space;zaba):

The tallest letter in ![equation](http://latex.codecogs.com/svg.latex?\inline&space;zaba) is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;z) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;h_z) is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;7). The selection area for this word is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;4&space;*&space;1mm&space;*&space;7mm&space;=&space;28mm^2).
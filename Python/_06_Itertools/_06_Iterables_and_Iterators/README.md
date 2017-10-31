The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

To read more about the functions in this module, check out their [documentation here](https://docs.python.org/2/library/itertools.html).

You are given a list of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lowercase English letters. For a given integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;K), you can select any ![equation](http://latex.codecogs.com/svg.latex?\inline&space;K) indices (assume ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1)-based indexing) with a uniform probability from the list.

Find the probability that at least one of the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;K) indices selected will contain the letter: '![equation](http://latex.codecogs.com/svg.latex?\inline&space;a)'.

__Input Format__

The input consists of three lines. The first line contains the integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N), denoting the length of the list. The next line consists of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) space-separated lowercase English letters, denoting the elements of the list.

The third and the last line of input contains the integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;K), denoting the number of indices to be selected.

__Output Format__

Output a single line consisting of the probability that at least one of the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;K) indices selected contains the letter:'![equation](http://latex.codecogs.com/svg.latex?\inline&space;a)'.

__Note:__ The answer must be correct up to 3 decimal places.

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20N%20%5Cleq%2010)

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20K%20%5Cleq%20N)

All the letters in the list are lowercase English letters.

__Sample Input__
```commandline
4 
a a c d
2
```
__Sample Output__
```commandline
0.8333
```
__Explanation__

All possible unordered tuples of length ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) comprising of indices from ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1) to ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4) are: <br>
![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20%281%2C%202%29%2C%20%281%2C%203%29%2C%20%281%2C%204%29%2C%20%282%2C%203%29%2C%20%282%2C%204%29%2C%20%283%2C%204%29)

Out of these ![equation](http://latex.codecogs.com/svg.latex?\inline&space;6) combinations, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;5) of them contain either index ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1) or index ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) which are the indices that contain the letter '![equation](http://latex.codecogs.com/svg.latex?\inline&space;a)'.

Hence, the answer is ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20%5Cfrac%7B5%7D%7B6%7D).
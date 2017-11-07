You are given  words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

__Note__: Each input line ends with a __"\n"__ character.

__Constraints:__ 

 ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20n%20%5Cleq%2010%5E5) <br>
The sum of the lengths of all the words do not exceed ![equation](http://latex.codecogs.com/svg.latex?\inline&space;10^6) <br>
All the words are composed of lowercase English letters only.

__Input Format__

The first line contains the integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n). <br>
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) lines each contain a word.

__Output Format__

Output ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) lines. <br>
On the first line, output the number of distinct words from the input. <br>
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

__Sample Input__
```commandline
4
bcdef
abcdefg
bcde
bcdef
```
__Sample Output__
```commandline
3
2 1 1
```
__Explanation__

There are ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3) distinct words. Here, __"bcdef"__ appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are __"bcdef"__, __"abcdefg"__ and __"bcde"__ which corresponds to the output.
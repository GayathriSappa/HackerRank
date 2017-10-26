Kevin and Stuart want to play the __'The Minion Game'__.

__Game Rules__

Both players are given the same string, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S).<br>
Both players have to make substrings using the letters of the string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S).<br>
Stuart has to make words starting with consonants.<br>
Kevin has to make words starting with vowels.<br> 
The game ends when both players have made all possible substrings. 

__Scoring__<br>
A player gets +1 point for each occurrence of the substring in the string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S).

__For Example:__
String ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S) = BANANA<br>
Kevin's vowel beginning word = ANA<br>
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 

For better understanding, see the image below: 

![](https://github.com/avtomato/HackerRank/blob/master/Python/img/1450330231-04db904008-banana.png)

Your task is to determine the winner of the game and their score.

__Input Format__

A single line of input containing the string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S). 
__Note:__ The string ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S) will contain only uppercase letters: ![equation](http://latex.codecogs.com/svg.latex?\inline&space;[A-Z]).

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?\inline&space;0&space;<&space;len(S)&space;\leq&space;10^6)

__Output Format__

Print one line: the name of the winner and their score separated by a space.

If the game is a draw, print Draw.

__Sample Input__
```commandline
BANANA
```
__Sample Output__
```commandline
Stuart 12
```
__Note : 
Vowels are only defined as ![equation](http://latex.codecogs.com/svg.latex?\inline&space;AEIOU). In this problem, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;Y) is not considered a vowel__.

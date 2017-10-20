Julius Caesar protected his confidential information by encrypting it in a cipher. Caesar's cipher rotated every letter in a string by a fixed number, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;K), making it unreadable by his enemies. Given a string, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S), and a number, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;K), encrypt ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S) and print the resulting string.

__Note:__ The cipher only encrypts letters; symbols, such as -, remain unencrypted.

__Input Format__

The first line contains an integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N), which is the length of the unencrypted string. 
The second line contains the unencrypted string, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;S). 
The third line contains the integer encryption key, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;K), which is the number of letters to rotate.

__Constraints__ 
 
![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\leq&space;N&space;\leq&space;100)<br>
![equation](https://latex.codecogs.com/svg.latex?\inline&space;0&space;\leq&space;K&space;\leq&space;100)<br>
![equation](http://latex.codecogs.com/svg.latex?\inline&space;S) is a valid ASCII string and doesn't contain any spaces.

__Output Format__

For each test case, print the encoded string.

__Sample Input__
```commandline
11
middle-Outz
2
```
__Sample Output__
```commandline
okffng-Qwvb
```
__Explanation__

Each unencrypted letter is replaced with the letter occurring ![equation](http://latex.codecogs.com/svg.latex?\inline&space;K) spaces after it when listed alphabetically. Think of the alphabet as being both case-sensitive and circular; if ![equation](http://latex.codecogs.com/svg.latex?\inline&space;K) rotates past the end of the alphabet, it loops back to the beginning (i.e.: the letter after ![equation](http://latex.codecogs.com/svg.latex?\inline&space;z) is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a), and the letter after ![equation](http://latex.codecogs.com/svg.latex?\inline&space;Z) is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A)).

__Selected Examples:__<br> 
![equation](http://latex.codecogs.com/svg.latex?\inline&space;m) (ASCII 109) becomes ![equation](http://latex.codecogs.com/svg.latex?\inline&space;0) (ASCII 111).<br> 
![equation](http://latex.codecogs.com/svg.latex?\inline&space;i) (ASCII 105) becomes ![equation](http://latex.codecogs.com/svg.latex?\inline&space;k) (ASCII 107).<br> 
![equation](http://latex.codecogs.com/svg.latex?\inline&space;-) remains the same, as symbols are not encoded.<br> 
![equation](http://latex.codecogs.com/svg.latex?\inline&space;O) (ASCII 79) becomes ![equation](http://latex.codecogs.com/svg.latex?\inline&space;Q) (ASCII 81).<br> 
![equation](http://latex.codecogs.com/svg.latex?\inline&space;z) (ASCII 122) becomes ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b) (ASCII 98); because ![equation](http://latex.codecogs.com/svg.latex?\inline&space;z) is the last letter of the alphabet, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a) (ASCII 97) is the next letter after it in lower-case rotation.
Steve has a string, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s), consisting of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) lowercase English alphabetic letters. In one operation, he can delete any pair of adjacent letters with same value. For example, string "aabcc" would become either "aab" or "bcc" after ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1) operation.

Steve wants to reduce ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s) as much as possible. To do this, he will repeat the above operation as many times as it can be performed. Help Steve out by finding and printing ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s)'s non-reducible form!

__Note:__ If the final string is empty, print Empty String .

__Input Format__

A single string, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s).

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\le&space;n&space;\le&space;100)

__Output Format__

If the final string is empty, print Empty String; otherwise, print the final non-reducible string.

__Sample Input 0__
```commandline
aaabccddd
```
__Sample Output 0__
```commandline
abd
```
__Sample Case 0__

Steve can perform the following sequence of operations to get the final string:

1. aaabccddd → abccddd
2. abccddd → abddd
3. abddd → abd

Thus, we print abd.

__Sample Input 1__
```commandline
baab
```
__Sample Output 1__
```commandline
Empty String
```
__Explanation 1__

Steve can perform the following sequence of operations to get the final string:

1. baab → bb
2. bb → Empty String

Thus, we print Empty String.

__Sample Input 2__
```commandline
aa
```
__Sample Output 2__
```commandline
Empty String
```
__Explanation 2__

Steve can perform the following sequence of operations to get the final string:

1. aa → Empty String

Thus, we print Empty String.
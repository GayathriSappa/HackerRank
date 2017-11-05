You and Fredrick are good friends. Yesterday, Fredrick received ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) credit cards from __ABCD Bank__. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from __ABCD Bank__ has the following characteristics: 

► It must start with a ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;5) or ![equation](http://latex.codecogs.com/svg.latex?\inline&space;6). <br>
► It must contain exactly ![equation](http://latex.codecogs.com/svg.latex?\inline&space;16) digits. <br>
► It must only consist of digits (![equation](http://latex.codecogs.com/svg.latex?\inline&space;0)-![equation](http://latex.codecogs.com/svg.latex?\inline&space;9)). <br>
► It may have digits in groups of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4), separated by one hyphen "-". <br>
► It must NOT use any other separator like ' ' , '_', etc. <br>
► It must NOT have ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4) or more consecutive repeated digits.

__Examples:__

Valid Credit Card Numbers
```commandline
4253625879615786
4424424424442444
5122-2368-7954-3214
```
Invalid Credit Card Numbers
```commandline
42536258796157867       #17 digits in card number → Invalid 
4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
44244x4424442444        #Contains non digit characters → Invalid
0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid
```
__Input Format__

The first line of input contains an integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N). <br> 
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines contain credit card numbers.

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20N%20%3C%20100)

__Output Format__

Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'. Do not print the quotes.

__Sample Input__
```commandline
6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456
```
__Sample Output__
```commandline
Valid
Valid
Invalid
Valid
Invalid
Invalid
```
__Explanation__

4123456789123456 : __Valid__ <br>
5123-4567-8912-3456 : __Valid__ <br>
61234-![equation](http://latex.codecogs.com/svg.latex?\inline&space;567)-8912-3456 : __Invalid__, because the card number is not divided into equal groups of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4). <br>
4123356789123456 : __Valid__ <br>
51![equation](http://latex.codecogs.com/svg.latex?\inline&space;33)-![equation](http://latex.codecogs.com/svg.latex?\inline&space;33)67-8912-3456 : __Invalid__, consecutive digits ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3333) is repeating ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4) times. <br>
5123 - 4567 - 8912 - 3456 : __Invalid__, because space '  ' and - are used as separators.
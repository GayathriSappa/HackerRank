CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).

Specifications of HEX Color Code

■ It must start with a '#' symbol. <br>
■ It can have ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3) or ![equation](http://latex.codecogs.com/svg.latex?\inline&space;6) digits. <br>
■ Each digit is in the range of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;0) to ![equation](http://latex.codecogs.com/svg.latex?\inline&space;F). (![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%2C%201%2C%202%2C%203%2C%204%2C%205%2C%206%2C%207%2C%208%2C%209%2C%200%2C%20A%2C%20B%2C%20C%2C%20D%2C%20E) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;F)). <br>
■ ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20A%20-%20F) letters can be lower case. (![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20a%2C%20b%2C%20c%2C%20d%2C%20e) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;f) are also valid digits).

__Examples__
```commandline
Valid Hex Color Codes
#FFF 
#025 
#F0A1FB 

Invalid Hex Color Codes
#fffabg
#abcf
#12365erff
```
You are given ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.

CSS Code Pattern

```commandline
Selector
{
	Property: Value;
}
```
__Input Format__

The first line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N), the number of code lines.
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines contains CSS Codes.

__Constraints__

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20N%20%3C%2050)

__Output Format__

Output the color codes with '#' symbols on separate lines.

__Sample Input__
```commandline
11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
} 
```  
__Sample Output__
```commandline
#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff
```
__Explanation__

\#BED and #Cab satisfy the Hex Color Code criteria, but they are used as selectors and not as color codes in the given CSS. 

Hence, the valid color codes are:

\#FfFdF8 <br>
\#aef <br>
\#f9f9f9 <br>
\#fff <br>
\#ABC <br>
\#fff

__Note:__ There are no comments ( // or /* */) in CSS Code.
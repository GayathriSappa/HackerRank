An English text needs to be encrypted using the following encryption scheme.<br> 
First, the spaces are removed from the text. Let ![equation](http://latex.codecogs.com/svg.latex?\inline&space;L) be the length of this text.<br> 
Then, characters are written into a grid, whose rows and columns have the following constraints:

* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;\left&space;\lfloor&space;\sqrt{L}&space;\right&space;\rfloor\leq&space;row&space;\leq&space;column&space;\leq&space;\left&space;\lceil&space;\sqrt{L}&space;\right&space;\rceil), where ![equation](https://latex.codecogs.com/svg.latex?\inline&space;\left&space;\lfloor&space;x&space;\right&space;\rfloor) is floor function and ![equation](https://latex.codecogs.com/svg.latex?\inline&space;\left&space;\lceil&space;x&space;\right&space;\rceil) is ceil function

For example, the sentence if man was meant to stay on the ground god would have given us roots after removing spaces is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;54) characters long, so it is written in the form of a grid with 7 rows and 8 columns.
```commandline
ifmanwas  
meanttos          
tayonthe  
groundgo  
dwouldha  
vegivenu  
sroots
```
* Ensure that ![equation](https://latex.codecogs.com/svg.latex?\inline&space;rows&space;\times&space;columns&space;\geq&space;L)
* If multiple grids satisfy the above conditions, choose the one with the minimum area, i.e. ![equation](https://latex.codecogs.com/svg.latex?\inline&space;rows&space;\times&space;columns).

The encoded message is obtained by displaying the characters in a column, inserting a space, and then displaying the next column and inserting a space, and so on. For example, the encoded message for the above rectangle is:
```commandline
imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau
```
You will be given a message in English with no spaces between the words. The maximum message length can be ![equation](http://latex.codecogs.com/svg.latex?\inline&space;81) characters. Print the encoded message.

Here are some more examples:

__Sample Input:__
```commandline
haveaniceday
```
__Sample Output:__
```commandline
hae and via ecy
```
__Sample Input:__
```commandline
feedthedog 
```   
__Sample Output:__
```commandline
fto ehg ee dd
```
__Sample Input:__
```commandline
chillout
```
__Sample Output:__
```commandline
clu hlt io
```
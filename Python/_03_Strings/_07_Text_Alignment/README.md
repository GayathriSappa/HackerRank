n Python, a string of text can be aligned left, right and center.

__.ljust(width)__

This method returns a left aligned string of length width.
```python
>>> width = 20
>>> print 'HackerRank'.ljust(width,'-')
HackerRank----------  
```
__.center(width)__

This method returns a centered string of length width.
```python
>>> width = 20
>>> print 'HackerRank'.center(width,'-')
-----HackerRank-----
```
__.rjust(width)__

This method returns a right aligned string of length width.
```python
>>> width = 20
>>> print 'HackerRank'.rjust(width,'-')
----------HackerRank
```
__Task__

You are given a partial code that is used for generating the HackerRank Logo of variable thickness.<br> 
Your task is to replace the blank (______) with rjust, ljust or center.

__Input Format__

A single line containing the thickness value for the logo.

__Constraints__

The thickness must be an odd number.<br>
![equation](https://latex.codecogs.com/svg.latex?\inline&space;0&space;<&space;thickness&space;<&space;50)

__Output Format__

Output the desired logo.

__Sample Input__
```commandline
5
```
__Sample Output__
```commandline

    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H 
```
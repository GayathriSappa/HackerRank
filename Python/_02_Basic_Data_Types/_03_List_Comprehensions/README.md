Let's learn about list comprehensions! You are given three integers ![equation](https://latex.codecogs.com/svg.latex?\inline&space;X,&space;Y) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;Z) representing the dimensions of a cuboid along with an integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N). You have to print a list of all possible coordinates given by ![equation](http://latex.codecogs.com/svg.latex?\inline&space;(i,j,k)) on a 3D grid where the sum of ![equation](https://latex.codecogs.com/svg.latex?\inline&space;i&space;&plus;&space;j&space;&plus;&space;k) is not equal to ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N). Here, ![equation](https://latex.codecogs.com/svg.latex?\inline&space;0&space;\leq&space;i&space;\leq&space;X;0&space;\leq&space;j&space;\leq&space;Y;0&space;\leq&space;k&space;\leq&space;Z) 

__Input Format__

Four integers ![equation](https://latex.codecogs.com/svg.latex?\inline&space;X,&space;Y,&space;Z) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) each on four separate lines, respectively.

__Constraints__

Print the list in lexicographic increasing order.

__Sample Input__
```commandline
1
1
1
2
```
__Sample Output__
```commandline
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
``` 
__Explanation__

__Concept__

You have already used lists in previous hacks. List comprehensions are an elegant way to build a list without having to use different for loops to append values one by one. This example might help.

__Example:__ You are given two integers x and y . You need to find out the ordered pairs ( i , j ) , such that ( i + j ) is not equal to n and print them in lexicographic order.( 0 <= i <= x ) and ( 0 <= j <= y) This is the code if __we dont use list comprehensions in Python__.
```python
x = int ( raw_input())
y = int ( raw_input())
n = int ( raw_input())
ar = []
p = 0
for i in range ( x + 1 ) :
    for j in range( y + 1):
        if i+j != n:
            ar.append([])
            ar[p] = [ i , j ]
            p+=1
print ar 
```   
Other smaller codes may also exist, but using list comprehensions is always a good option. __Code using list comprehensions:__
```python
x = int ( raw_input())
y = int ( raw_input())
n = int ( raw_input())
print [ [ i, j] for i in range( x + 1) for j in range( y + 1) if ( ( i + j ) != n )]
```
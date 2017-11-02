[zip([iterable, ...])](https://docs.python.org/2/library/functions.html#zip)

This function returns a list of tuples. The ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i^{th}) tuple contains the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i^{th}) element from each of the argument sequences or iterables.

If the argument sequences are of unequal lengths, then the returned list is truncated to the length of the shortest argument sequence.

__Sample Code__
```python
>>> print zip([1,2,3,4,5,6],'Hacker')
[(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k'), (5, 'e'), (6, 'r')]
>>> 
>>> print zip([1,2,3,4,5,6],[0,9,8,7,6,5,4,3,2,1])
[(1, 0), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5)]
>>> 
>>> A = [1,2,3]
>>> B = [6,5,4]
>>> C = [7,8,9]
>>> X = [A] + [B] + [C]
>>> 
>>> print zip(*X)
[(1, 6, 7), (2, 5, 8), (3, 4, 9)]
```
__Task__

The National University conducts an examination of ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) students in ![equation](http://latex.codecogs.com/svg.latex?\inline&space;X) subjects. <br>
Your task is to compute the average scores of each student.

![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20Average%5C%20score%20%3D%20%5Cfrac%7BSum%5C%20of%5C%20scores%5C%20obtained%5C%20in%5C%20all%5C%20subjects%5C%20by%5C%20a%5C%20student%7D%7BTotal%5C%20number%5C%20of%5C%20subjects%7D)

The format for the general mark sheet is:
```commandline
Student ID → ___1_____2_____3_____4_____5__               
Subject 1   |  89    90    78    93    80
Subject 2   |  90    91    85    88    86  
Subject 3   |  91    92    83    89    90.5
            |______________________________
Average        90    91    82    90    85.5
``` 
__Input Format__

The first line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;X) separated by a space. <br>
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;X) lines contains the space separated marks obtained by students in a particular subject.

__Constraints__

 ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20N%20%5Cleq%20100)<br>
 ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20X%20%5Cleq%20100)

__Output Format__

Print the averages of all students on separate lines.

The averages must be correct up to ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1) decimal place.

__Sample Input__
```commandline
5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5
```
__Sample Output__
```commandline
90.0 
91.0 
82.0 
90.0 
85.5  
```      
__Explanation__

Marks obtained by __student 1__: ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%2089%2C%2090%2C%2091) <br> 
Average marks of __student 1__: ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20270/3%20%3D%2090)

Marks obtained by __student 2__: ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%2090%2C%2091%2C%2092) <br> 
Average marks of __student 2__: ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20273/3%20%3D%2091)

Marks obtained by __student 3__: ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%2078%2C%2085%2C%2083) <br> 
Average marks of __student 3__: ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20246/3%20%3D%2082)

Marks obtained by __student 4__: ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%2093%2C%2088%2C%2089) <br> 
Average marks of __student 4__: ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20270/3%20%3D%2090)

Marks obtained by __student 5__: ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%2080%2C%2086%2C%2090.5) <br> 
Average marks of __student 5__: ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20256.5/3%20%3D%2085.5)


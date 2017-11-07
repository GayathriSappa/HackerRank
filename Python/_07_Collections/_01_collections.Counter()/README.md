[collections.Counter()](https://docs.python.org/2/library/collections.html#collections.Counter) 

A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

__Sample Code__
```python
>>> from collections import Counter
>>> 
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>> 
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>>> 
>>> print Counter(myList).values()
[3, 4, 4, 2, 1]
```
__Task__

![equation](http://latex.codecogs.com/svg.latex?\inline&space;Raghu) is a shoe shop owner. His shop has ![equation](http://latex.codecogs.com/svg.latex?\inline&space;X) number of shoes. <br>
He has a list containing the size of each shoe he has in his shop. <br>
There are ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) number of customers who are willing to pay ![equation](http://latex.codecogs.com/svg.latex?\inline&space;x_i) amount of money only if they get the shoe of their desired size.

Your task is to compute how much money ![equation](http://latex.codecogs.com/svg.latex?\inline&space;Raghu) earned.

__Input Format__

The first line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;X), the number of shoes. <br>
The second line contains the space separated list of all the shoe sizes in the shop. <br>
The third line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N), the number of customers. <br>
The next ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines contain the space separated values of the ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20shoe%5C%20size) desired by the customer and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;x_i), the price of the shoe.

__Constraints__

 ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20X%20%3C%2010%5E3) <br>
 ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20N%20%5Cleq%2010%5E3) <br>
 ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%2020%20%3C%20x_i%20%3C%20100) <br>
 ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%202%20%3C%20shoe%5C%20size%20%3C%2020) 

__Output Format__

Print the amount of money earned by ![equation](http://latex.codecogs.com/svg.latex?\inline&space;Raghu).

__Sample Input__
```commandline
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
```
__Sample Output__
```commandline
200
```
__Explanation__

__Customer 1__: Purchased size 6 shoe for __$55__. <br>
__Customer 2__: Purchased size 6 shoe for __$45__. <br>
__Customer 3__: Size 6 no longer available, so no purchase. <br>
__Customer 4__: Purchased size 4 shoe for __$40__. <br>
__Customer 5__: Purchased size 18 shoe for __$60__. <br>
__Customer 6__: Size 10 not available, so no purchase.

Total money earned = ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%2055%20&plus;%2045%20&plus;%2060%20&plus;%2040%20%3D)![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20%5C%24200) 
HackerLand Enterprise is adopting a new viral advertising strategy. When they launch a new product, they advertise it to exactly ![equation](http://latex.codecogs.com/svg.latex?\inline&space;5) people on social media.

On the first day, half of those ![equation](http://latex.codecogs.com/svg.latex?\inline&space;5) people (i.e., ![equation](https://latex.codecogs.com/svg.latex?\inline&space;floor\left&space;(&space;\frac{5}{2}&space;\right&space;)&space;=&space;2)) like the advertisement and each person shares it with ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3) of their friends; the remaining people (i.e., ![equation](https://latex.codecogs.com/svg.latex?\inline&space;5&space;-&space;floor\left&space;(&space;\frac{5}{2}&space;\right&space;)&space;=&space;3)) delete the advertisement because it doesn't interest them. So, at the beginning of the second day, ![equation](https://latex.codecogs.com/svg.latex?\inline&space;floor\left&space;(&space;\frac{5}{2}&space;\right&space;)&space;\times&space;3&space;=&space;2&space;\times&space;3&space;=&space;6) people receive the advertisement.

On the second day, half of the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;6) people who received the advertisement share it with ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3) new friends. So, at the beginning of the third day, ![equation](https://latex.codecogs.com/svg.latex?\inline&space;floor\left&space;(&space;\frac{6}{2}&space;\right&space;)&space;\times&space;3&space;=&space;3&space;\times&space;3&space;=&space;9) people receive the advertisement. The diagram below depicts the advertisement's virality over the first three days (green denotes a person that likes the advertisement and red denotes a person that disliked and deleted it):

![](https://github.com/avtomato/HackerRank/blob/master/Algorithms/img/1475677928-3788004924-strangead.png)

Assume that at the beginning of the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i^{th}) day, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;m) people received the advertisement, ![equation](https://latex.codecogs.com/svg.latex?\inline&space;floor\left&space;(&space;\frac{m}{2}&space;\right&space;)) people like and share it with ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3) new friends, and ![equation](https://latex.codecogs.com/svg.latex?\inline&space;m&space;-&space;floor\left&space;(&space;\frac{m}{2}&space;\right&space;)) people dislike and delete it. At the beginning of the ![equation](https://latex.codecogs.com/svg.latex?\inline&space;(i&space;&plus;&space;1)^{th}) day, ![equation](https://latex.codecogs.com/svg.latex?\inline&space;floor\left&space;(&space;\frac{m}{2}&space;\right&space;)&space;\times&space;3) people receive the advertisement.

Given an integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n), find and print the total number of people who liked HackerLand Enterprise's advertisement during the first ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) days. It is guaranteed that no two people have any friends in common and, after a person shares the advertisement with a friend, the friend always sees it the next day.

__Input Format__

A single integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n), denoting a number of days.

__Constraints__

* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\leq&space;n&space;\leq&space;50)

__Output Format__

Print the number of people who liked the advertisement during the first ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) days.

__Sample Input__
```commandline
3
```
__Sample Output__
```commandline
9
```
__Explanation__

This example is depicted by the diagram at the top of the challenge. ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) people liked the advertisement on the first day, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3) people liked the advertisement on the second day and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4) people liked the advertisement on the third day, so the answer is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;2&space;&plus;&space;3&space;&plus;&space;4&space;=&space;9).
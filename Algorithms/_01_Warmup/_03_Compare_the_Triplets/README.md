Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1) to ![equation](http://latex.codecogs.com/svg.latex?\inline&space;100) for three categories: problem clarity, originality, and difficulty.

We define the rating for Alice's challenge to be the triplet ![equation](https://latex.codecogs.com/svg.latex?\inline&space;A&space;=&space;(a_0,&space;a_1,&space;a_2)), and the rating for Bob's challenge to be the triplet ![equation](https://latex.codecogs.com/svg.latex?\inline&space;B&space;=&space;(b_0,&space;b_1,&space;b_2)).

Your task is to find their comparison points by comparing ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a_0) with ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b_0), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a_1) with ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b_1), and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a_2) with ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b_2).

* If ![equation](https://latex.codecogs.com/svg.latex?\inline&space;a_i&space;>&space;b_i), then Alice is awarded  point.
* If ![equation](https://latex.codecogs.com/svg.latex?\inline&space;a_i&space;<&space;b_i), then Bob is awarded  point.
* If ![equation](https://latex.codecogs.com/svg.latex?\inline&space;a_i&space;=&space;b_i), then neither person receives a point.

Comparison points is the total points a person earned.

Given ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A) and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B), can you compare the two challenges and print their respective comparison points?

__Input Format__<br>
The first line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3) space-separated integers, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a_0), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a_1), and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;a_2), describing the respective values in triplet ![equation](http://latex.codecogs.com/svg.latex?\inline&space;A).<br> 
The second line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3) space-separated integers, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b_0), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b_1), and ![equation](http://latex.codecogs.com/svg.latex?\inline&space;b_2), describing the respective values in triplet ![equation](http://latex.codecogs.com/svg.latex?\inline&space;B).

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\le&space;a_i&space;\le&space;100)
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\le&space;b_i&space;\le&space;100)

__Output Format__<br>
Print two space-separated integers denoting the respective comparison points earned by Alice and Bob.

__Sample Input__
```commandline
5 6 7
3 6 10
```
__Sample Output__
```commandline
1 1
```
__Explanation__

In this example:
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;A&space;=&space;(a_0,&space;a_1,&space;a_2)&space;=&space;(5,&space;6,&space;7))
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;B&space;=&space;(b_0,&space;b_1,&space;b_2)&space;=&space;(5,&space;6,&space;10))

Now, let's compare each individual score:

* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;a_0&space;>&space;b_0), so Alice receives ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1) point.
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;a_1&space;=&space;b_1), so nobody receives a point.
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;a_2&space;<&space;b_2), so Bob receives ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1) point.

Alice's comparison score is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1), and Bob's comparison score is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1). Thus, we print 1 1 (Alice's comparison score followed by Bob's comparison score) on a single line.

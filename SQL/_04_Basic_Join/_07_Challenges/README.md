Julia asked her students to create some coding challenges. Write a query to print the hacker_id, name, and the total number of challenges created by each student. Sort your results by the total number of challenges in descending order. If more than one student created the same number of challenges, then sort the result by hacker_id. If more than one student created the same number of challenges and the count is less than the maximum number of challenges created, then exclude those students from the result.

__Input Format__

The following tables contain challenge data:

* Hackers: The hacker_id is the id of the hacker, and name is the name of the hacker.<br> 
![](https://github.com/avtomato/HackerRank/blob/master/SQL/img/1458521004-cb4c077dd3-ScreenShot2016-03-21at6.06.54AM.png)
* Challenges: The challenge_id is the id of the challenge, and hacker_id is the id of the student who created the challenge.<br> 
![](https://github.com/avtomato/HackerRank/blob/master/SQL/img/1458521079-549341d9ec-ScreenShot2016-03-21at6.07.03AM.png)

__Sample Input 0__

Hackers Table:<br>
![](https://github.com/avtomato/HackerRank/blob/master/SQL/img/1458521384-34c6866dae-ScreenShot2016-03-21at6.07.15AM.png)<br> 
Challenges Table:<br>
![](https://github.com/avtomato/HackerRank/blob/master/SQL/img/1458521410-befa8e1cd9-ScreenShot2016-03-21at6.07.25AM.png)

__Sample Output 0__
```commandline
21283 Angela 6
88255 Patrick 5
96196 Lisa 1
```
__Sample Input 1__

Hackers Table:<br>
![](https://github.com/avtomato/HackerRank/blob/master/SQL/img/1458521469-87036deea3-ScreenShot2016-03-21at6.07.48AM.png)<br> 
Challenges Table:<br>
![](https://github.com/avtomato/HackerRank/blob/master/SQL/img/1458521490-358215cf0b-ScreenShot2016-03-21at6.07.58AM.png)

__Sample Output 1__
```commandline
12299 Rose 6
34856 Angela 6
79345 Frank 4
80491 Patrick 3
81041 Lisa 1
```
__Explanation__

For Sample Case 0, we can get the following details: 

![](https://github.com/avtomato/HackerRank/blob/master/SQL/img/1458521677-fd04c384c0-ScreenShot2016-03-21at6.07.38AM.png)<br>
Students ![equation](https://latex.codecogs.com/svg.latex?\inline&space;5077) and ![equation](https://latex.codecogs.com/svg.latex?\inline&space;62743) both created ![equation](https://latex.codecogs.com/svg.latex?\inline&space;4) challenges, but the maximum number of challenges created is ![equation](https://latex.codecogs.com/svg.latex?\inline&space;6) so these students are excluded from the result.

For Sample Case 1, we can get the following details:

![](https://github.com/avtomato/HackerRank/blob/master/SQL/img/1458521836-24039e7523-ScreenShot2016-03-21at6.08.08AM.png)<br>
Students ![equation](https://latex.codecogs.com/svg.latex?\inline&space;12299) and ![equation](https://latex.codecogs.com/svg.latex?\inline&space;34856) both created ![equation](https://latex.codecogs.com/svg.latex?\inline&space;6) challenges. Because ![equation](https://latex.codecogs.com/svg.latex?\inline&space;6) is the maximum number of challenges created, these students are included in the result.

You did such a great job helping Julia with her last coding contest challenge that she wants you to work on this one, too!

The total score of a hacker is the sum of their maximum scores for all of the challenges. Write a query to print the hacker_id, name, and total score of the hackers ordered by the descending score. If more than one hacker achieved the same total score, then sort the result by ascending hacker_id. Exclude all hackers with a total score of ![equation](https://latex.codecogs.com/svg.latex?\inline&space;0) from your result.

__Input Format__

The following tables contain contest data:

* Hackers: The hacker_id is the id of the hacker, and name is the name of the hacker.<br> 
![](https://github.com/avtomato/HackerRank/blob/master/SQL/img/1458522826-a9ddd28469-ScreenShot2016-03-21at6.40.27AM.png)
* Submissions: The submission_id is the id of the submission, hacker_id is the id of the hacker who made the submission, challenge_id is the id of the challenge for which the submission belongs to, and score is the score of the submission.<br> 
![](https://github.com/avtomato/HackerRank/blob/master/SQL/img/1458523022-771511df90-ScreenShot2016-03-21at6.40.37AM.png)

__Sample Input__

Hackers Table:<br> 
![](https://github.com/avtomato/HackerRank/blob/master/SQL/img/1458523374-7ecc39010f-ScreenShot2016-03-21at6.51.56AM.png)<br>
Submissions Table:<br>
![](https://github.com/avtomato/HackerRank/blob/master/SQL/img/1458523388-0896218137-ScreenShot2016-03-21at6.51.45AM.png)

__Sample Output__
```commandline
4071 Rose 191
74842 Lisa 174
84072 Bonnie 100
4806 Angela 89
26071 Frank 85
80305 Kimberly 67
49438 Patrick 43
```
__Explanation__

Hacker 4071 submitted solutions for challenges 19797 and 49593, so the total score ![equation](https://latex.codecogs.com/svg.latex?\inline&space;=&space;95&space;&plus;&space;max(43,96)&space;=&space;191).

Hacker 74842 submitted solutions for challenges 19797 and 63132, so the total score ![equation](https://latex.codecogs.com/svg.latex?\inline&space;=&space;max(98,5)&space;&plus;&space;76&space;=&space;174)

Hacker 84072 submitted solutions for challenges 49593 and 63132, so the total score ![equation](https://latex.codecogs.com/svg.latex?\inline&space;=&space;100&space;&plus;&space;0&space;=&space;100).

The total scors for hackers 4806, 26071, 80305, and 49438 can be similarly calculated.

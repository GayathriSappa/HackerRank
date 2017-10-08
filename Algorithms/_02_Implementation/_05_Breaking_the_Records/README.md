Maria plays ![equation](https://latex.codecogs.com/svg.latex?\inline&space;n) games of college basketball in a season. Because she wants to go pro, she tracks her points scored per game sequentially in an array defined as ![equation](https://latex.codecogs.com/svg.latex?\inline&space;score&space;=&space;s_0,&space;s_1,&space;...,&space;s_{n-1}). After each game ![equation](https://latex.codecogs.com/svg.latex?\inline&space;i), she checks to see if score ![equation](https://latex.codecogs.com/svg.latex?\inline&space;s_i) breaks her record for most or least points scored so far during that season.

Given Maria's array of ![equation](https://latex.codecogs.com/svg.latex?\inline&space;scores) for a season of ![equation](https://latex.codecogs.com/svg.latex?\inline&space;n) games, find and print the number of times she breaks her record for most and least points scored during the season.

__Note:__ Assume her records for most and least points at the start of the season are the number of points scored during the first game of the season.

__Input Format__

The first line contains an integer denoting ![equation](https://latex.codecogs.com/svg.latex?\inline&space;n) (the number of games). 
The second line contains ![equation](https://latex.codecogs.com/svg.latex?\inline&space;n) space-separated integers describing the respective values of ![equation](https://latex.codecogs.com/svg.latex?\inline&space;s_0,&space;s_1,&space;...,&space;s_{n-1}).

__Constraints__
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\le&space;n&space;\le&space;1000)
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;0&space;\le&space;s_i&space;\le&space;10^8)

__Output Format__

Print two space-seperated integers describing the respective numbers of times her best (highest) score increased and her worst (lowest) score decreased.

__Sample Input 0__
```commandline
9
10 5 20 20 4 5 2 25 1
```
__Sample Output 0__
```commandline
2 4
```
__Explanation 0__

The diagram below depicts the number of times Maria broke her best and worst records throughout the season:

![](https://github.com/avtomato/HackerRank/blob/master/Algorithms/img/1487360234-6bca5c518d-breakingbest3.png)

She broke her best record twice (after games ![equation](https://latex.codecogs.com/svg.latex?\inline&space;2) and ![equation](https://latex.codecogs.com/svg.latex?\inline&space;7)) and her worst record four times (after games ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1), ![equation](https://latex.codecogs.com/svg.latex?\inline&space;4), ![equation](https://latex.codecogs.com/svg.latex?\inline&space;6), and ![equation](https://latex.codecogs.com/svg.latex?\inline&space;8)), so we print 2 4 as our answer. Note that she did not break her record for best score during game ![equation](https://latex.codecogs.com/svg.latex?\inline&space;3), as her score during that game was not strictly greater than her best record at the time.

__Sample Input 1__
```commandline
10
3 4 21 36 10 28 35 5 24 42
```
__Sample Output 1__
```commandline
4 0
```
__Explanation 1__

The diagram below depicts the number of times Maria broke her best and worst records throughout the season:

![](https://github.com/avtomato/HackerRank/blob/master/Algorithms/img/1487360375-aee4388234-breakingbest5.png)

She broke her best record four times (after games ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1), ![equation](https://latex.codecogs.com/svg.latex?\inline&space;2), ![equation](https://latex.codecogs.com/svg.latex?\inline&space;3), and ![equation](https://latex.codecogs.com/svg.latex?\inline&space;9)) and her worst record zero times (no score during the season was lower than the one she earned during her first game), so we print 4 0 as our answer.
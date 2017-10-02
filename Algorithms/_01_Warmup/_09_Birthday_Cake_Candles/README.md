Colleen is turning ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) years old! Therefore, she has ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) candles of various heights on her cake, and candle ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i) has height ![equation](http://latex.codecogs.com/svg.latex?\inline&space;height_i). Because the taller candles tower over the shorter ones, Colleen can only blow out the tallest candles.

Given the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;height_i) for each individual candle, find and print the number of candles she can successfully blow out.

__Input Format__<br>
The first line contains a single integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n), denoting the number of candles on the cake.<br> 
The second line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) space-separated integers, where each integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i) describes the height of candle ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i).

__Constraints__<br>
![equation](https://latex.codecogs.com/svg.latex?\inline&space;(1&space;\le&space;n&space;\le&space;10^5))<br>
![equation](https://latex.codecogs.com/svg.latex?\inline&space;(1&space;\le&space;height_i&space;\le&space;10^7))

__Output Format__<br>
Print the number of candles Colleen blows out on a new line.

__Sample Input 0__
```commandline
4
3 2 1 3
```
__Sample Output 0__
```commandline
2
```
__Explanation 0__

We have one candle of height ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1), one candle of height ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2), and two candles of height ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3). Colleen only blows out the tallest candles, meaning the candles where ![equation](https://latex.codecogs.com/svg.latex?\inline&space;height&space;=&space;3). Because there are ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) such candles, we print ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) on a new line.
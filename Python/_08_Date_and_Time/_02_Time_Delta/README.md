You are given 2 timestamps in the format given below:

```commandline
Day dd Mon yyyy hh:mm:ss +xxxx
```

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

__Input Format__

The first line contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;T), the number of testcases. <br> 
Each testcase contains ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) lines, representing time ![equation](http://latex.codecogs.com/svg.latex?\inline&space;t_1) and time ![equation](http://latex.codecogs.com/svg.latex?\inline&space;t_2).

__Constraints__

* Input contains only valid timestamps
* ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20year%20%5Cleq%203000).

__Output Format__

Print the absolute difference ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20%28t_1%20-%20t_2%29) in seconds.

__Sample Input 0__
```commandline
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
```
__Sample Output 0__
```commandline
25200
88200
```
__Explanation 0__

In the first query, when we compare the time in UTC for both the time stamps, we see a difference of 7 hours. which is ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%207%20%5Ctimes%203600) seconds or ![equation](http://latex.codecogs.com/svg.latex?\inline&space;25200) seconds.

Similarly, in the second query, time difference is 5 hours and 30 minutes for time zone adjusting for that we have a difference of 1 day and 30 minutes. Or ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%2024%20%5Ctimes%203600%20&plus;%2030%20%5Ctimes%2060%20%5CRightarrow%2088200)
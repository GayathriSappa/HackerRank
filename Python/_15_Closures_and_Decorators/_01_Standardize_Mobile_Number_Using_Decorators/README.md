Let's dive into decorators! You are given ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) mobile numbers. Sort them in ascending order then print them in the standard format shown below:

```commandline
+91 xxxxx xxxxx
```

The given mobile numbers may have ![equation](http://latex.codecogs.com/svg.latex?\inline&space;+91), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;91) or ![equation](http://latex.codecogs.com/svg.latex?\inline&space;0) written before the actual ![equation](http://latex.codecogs.com/svg.latex?\inline&space;10) digit number. Alternatively, there may not be any prefix at all. 

__Input Format__

The first line of input contains an integer ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N), the number of mobile phone numbers. <br>
![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) lines follow each containing a mobile number.

__Output Format__

Print ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) mobile numbers on separate lines in the required format.

__Sample Input__
```commandline
3
07895462130
919875641230
9195969878
```
__Sample Output__
```commandline
+91 78954 62130
+91 91959 69878
+91 98756 41230
```
__Concept__

Like most other programming languages, Python has the concept of closures. Extending these closures gives us decorators, which are an invaluable asset. You can learn about decorators in 12 easy steps [here](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/).<br>
To solve the above question, make a list of the mobile numbers and pass it to a function that sorts the array in ascending order. Make a decorator that standardizes the mobile numbers and apply it to the function.
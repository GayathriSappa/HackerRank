Вам задано число ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N). Найдите цифры этого числа, что делят ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N) и выведите их количество. При ![equation](https://latex.codecogs.com/svg.latex?\inline&space;N&space;=&space;24), у вас есть две цифры ![equation](https://latex.codecogs.com/svg.latex?\inline&space;-&space;2)  и ![equation](http://latex.codecogs.com/svg.latex?\inline&space;4). Обе эти цифры делят ![equation](http://latex.codecogs.com/svg.latex?\inline&space;24). Так что ответ  ![equation](https://latex.codecogs.com/svg.latex?\inline&space;-&space;2).

__Примечание__

* Если одна и та же цифра повторяется несколько раз на разных позициях, то её надо засчитать столько раз, сколько она повторяется, то есть, для ![equation](https://latex.codecogs.com/svg.latex?\inline&space;N&space;=&space;122), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) делит ![equation](http://latex.codecogs.com/svg.latex?\inline&space;122) и встречается на позициях разрядов единиц и десятков. Поэтому её надо засчитать два раза. Так что для этого примера ответ  ![equation](https://latex.codecogs.com/svg.latex?\inline&space;-&space;3).
* Деление на ![equation](http://latex.codecogs.com/svg.latex?\inline&space;0) не определено.

__Формат входных даных__
 
В первой строке записано количество тестов ![equation](http://latex.codecogs.com/svg.latex?\inline&space;T). 
В каждой из следующих ![equation](http://latex.codecogs.com/svg.latex?\inline&space;T) строк записано целое число ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N).

__Формат выходных даных__ 

Для каждого теста выведите в отдельной строке количество цифр числа ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N), что делят ![equation](http://latex.codecogs.com/svg.latex?\inline&space;N).

__Ограничения__ 
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;1&space;\le&space;T&space;\le&space;15) 
* ![equation](https://latex.codecogs.com/svg.latex?\inline&space;0&space;<&space;N&space;<&space;10^{10})

__Пример входных даных__
```commandline
2
12
1012
```
__Пример выходных даных__
```commandline
2
3
```
__Объяснение__

* Две цифры числа ![equation](http://latex.codecogs.com/svg.latex?\inline&space;12) делят его.
* ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1) делит ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1012) и встречается в двух позициях и ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2) в одной позиции. Деление на ![equation](http://latex.codecogs.com/svg.latex?\inline&space;0) не определено, так что его мы не засчитываем.

Эта задача была частью [Pragyan 12](http://www.pragyan.org/12/home/)
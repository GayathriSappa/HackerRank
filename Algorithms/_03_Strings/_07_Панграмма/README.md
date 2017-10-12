Вам задана строка ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s), состоящая из пробелов и латинских букв. Строка называется панграммой, если она содержит каждую из 26 латинских букв хотя бы раз. Определите является ли строка ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s) панграммой.

__Формат входных данных__

В единственной строке входных данных записана строка ![equation](https://latex.codecogs.com/svg.latex?\inline&space;s&space;(1&space;\leq&space;|s|&space;\leq&space;1000)). Строка может содержать только пробелы, заглавные и строчные буквы латинского алфавита. Заглавные и строчные буквы считаются одинаковыми.

__Формат выходных данных__

Выведите pangram если строка ![equation](http://latex.codecogs.com/svg.latex?\inline&space;s) является панграммой, иначе выведите not pangram.

__Пример входных данных #1__
```commandline
We promptly judged antique ivory buckles for the next prize
```    
__Пример выходных данных #1__
```commandline
pangram
```
__Пример входных данных #2__
```commandline
We promptly judged antique ivory buckles for the prize
```    
__Пример выходных данных #2__
```commandline
not pangram
```
__Пояснение__

Строка из первого примера является панграммой, потому что она содержит каждую букву латинского алфавита хотя бы один раз.
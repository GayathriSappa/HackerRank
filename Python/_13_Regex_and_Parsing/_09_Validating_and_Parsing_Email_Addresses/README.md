A valid email address meets the following criteria:

* It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
* The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: [alphanumeric characters](https://en.wikipedia.org/wiki/Alphanumeric), -,., and _.
* The domain and extension contain only [English alphabetical characters](https://en.wikipedia.org/wiki/English_alphabet).
* The extension is ![equation](http://latex.codecogs.com/svg.latex?\inline&space;1), ![equation](http://latex.codecogs.com/svg.latex?\inline&space;2), or ![equation](http://latex.codecogs.com/svg.latex?\inline&space;3) characters in length.

Given ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.

__Hint:__ Try using [Email.utils()](https://docs.python.org/2/library/email.util.html#module-email.utils) to complete this challenge. For example, this code:
```python
import email.utils
print email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>')
print email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com'))
```
produces this output:
```python
('DOSHI', 'DOSHI@hackerrank.com')
DOSHI <DOSHI@hackerrank.com>
```
__Input Format__

The first line contains a single integer, ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n), denoting the number of email address. <br>
Each line ![equation](http://latex.codecogs.com/svg.latex?\inline&space;i) of the ![equation](http://latex.codecogs.com/svg.latex?\inline&space;n) subsequent lines contains a name and an email address as two space-separated values following this format:
```commandline
name <user@email.com>
```
__Constraints__

* ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%3C%20n%20%3C%20100)

__Output Format__

Print the space-separated name and email address pairs containing valid email addresses only. Each pair must be printed on a new line in the following format:
```commandline
name <user@email.com>
```
You must print each valid email address in the same order as it was received as input.

__Sample Input__
```commandline
2  
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>
```
__Sample Output__
```commandline
DEXTER <dexter@hotmail.com>
```
__Explanation__

dexter@hotmail.com is a valid email address, so we print the name and email address pair received as input on a new line. <br>
virus!@variable.:p is not a valid email address because the username contains an exclamation point (!) and the extension contains a colon (:). As this email is not valid, we print nothing.
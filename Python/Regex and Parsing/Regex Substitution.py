import re


n = int(input())
s = """"""
for i in range(n):
    s += input()
    s += '\n'

m = re.search('\s&&\s', s)
n = re.search(r'\s\|\|\s', s)

while m or n:
    s = re.sub(r'\s&&\s', ' and ', s)
    s = re.sub(r'\s\|\|\s', ' or ', s)
    m = re.search('\s&&\s', s)
    n = re.search(r'\s\|\|\s', s)

print(s)

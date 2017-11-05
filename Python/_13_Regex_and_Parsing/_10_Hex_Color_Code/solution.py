import re


n = int(input())
s = """"""
regexp = re.compile(r'#[0-9a-f]{,6}(?=[,;)])|#[0-9a-f]{,3}(?=[,;)])', re.IGNORECASE)
for _ in range(n):
    temp = input() + '\n'
    s += temp

m = re.findall(regexp, s)
for i in m:
    print(i)

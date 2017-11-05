import re


T = int(input())
regexp = re.compile(r'^[-+]?[\d]*\.[\d]+$')

for i in range(T):
    N = input()
    print(bool(re.match(regexp, N)))

import re


T = int(input())
for _ in range(T):
    u = input()
    if len(u) != 10 or re.search(r'([A-Za-z0-9]).*\1', u):
        print('Invalid')
    elif re.search(r'(?<=[A-Z]).*[A-Z]', u) and re.search(r'(?<=[0-9]).*[0-9].*[0-9]', u) and re.match(r'[a-zA-Z0-9]', u):
        print("Valid")
    else:
        print('Invalid')

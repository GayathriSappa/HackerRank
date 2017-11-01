import re


T = int(input())
for _ in range(T):
    S = input()
    try:
        re.compile(r'{}'.format(S))
        print('True')
    except:
        print('False')

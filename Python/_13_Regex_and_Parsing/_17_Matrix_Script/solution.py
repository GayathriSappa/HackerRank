from itertools import chain
import re


N, M = map(int, input().split())
matrix = [input()for i in range(N)]

s = ''.join([i for i in chain(*zip(*matrix))])

regexp = re.compile(r'(?<=[A-Za-z0-9])([!@#$%& ])+(?=[a-zA-Z0-9])')
s = re.sub(regexp, ' ', s)
print(s)

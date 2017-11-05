
import re


P = input()
regexp = re.compile(r'([0-9])([0-9])\1')

print(bool(bool(re.match(r'^([0-9]){6}$', P)) and len(list(filter(lambda x: x, [bool(re.match(regexp, P[i:])) for i in range(len(P))]))) < 2))

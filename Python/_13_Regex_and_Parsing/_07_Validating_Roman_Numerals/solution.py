import re


s = input()
regexp = re.compile(r'^(M{0,3})(D?C{0,3}|C[DM])(L?X{0,3}|X[LC])(V?I{0,3}|I[VX])$')
print(bool(re.search(regexp, s)))

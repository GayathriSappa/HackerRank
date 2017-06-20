import re


s = input()
regexp = re.compile(r'([A-Za-z0-9])\1')
m = re.search(regexp, s)
print(m.group(1) if m else "-1")

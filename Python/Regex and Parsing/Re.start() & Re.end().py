import re


s = input()
k = input()
regexp = re.compile(r'%s' % k)

if not re.search(regexp, s):
    print((-1, -1))

for i in range(len(s)):
    m = re.match(regexp, s[i:])
    if m:
        print((m.start() + i, m.end() + i - 1))

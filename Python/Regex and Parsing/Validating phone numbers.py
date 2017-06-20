import re


n = int(input())
regexp = re.compile(r'^([789])(\d{9})$')

for _ in range(n):
    s = input()
    print("YES" if re.search(regexp, s) else "NO")

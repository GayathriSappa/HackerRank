import re


N = int(input())
regexp = re.compile(r'^[4-6][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$')
for _ in range(N):
    s = input()
    print('Valid' if re.search(regexp, s) and not re.search(r'([0-9])-?\1-?\1-?\1', s) else 'Invalid')

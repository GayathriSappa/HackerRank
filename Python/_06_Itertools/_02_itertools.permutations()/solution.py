from itertools import permutations

S, k = input().split()

[print(''.join(i)) for i in sorted(permutations(S, int(k)))]

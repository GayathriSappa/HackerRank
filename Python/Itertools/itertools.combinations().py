from itertools import combinations

S, k = input().split()

[[print(''.join(j)) for j in combinations(sorted(S), i)] for i in range(1, int(k)+1)]

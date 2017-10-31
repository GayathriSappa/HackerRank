from itertools import combinations


n = int(input())
ar = input().split()
k = int(input())

combinations_of_letters = [True if 'a' in i else False for i in combinations(ar, k)]
combinations_with_a = [i for i in combinations_of_letters if i]
print('{:.3}'.format(len(combinations_with_a) / len(combinations_of_letters)))

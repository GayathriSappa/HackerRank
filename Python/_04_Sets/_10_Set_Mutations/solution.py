n = int(input())
A = set(map(int, input().split()))
N = int(input())
for i in range(N):
    c, m = input().split()
    b = set(map(int, input().split()))
    if c in 'update':
        A.update(b)
    elif c in 'intersection_update':
        A.intersection_update(b)
    elif c in 'difference_update':
        A.difference_update(b)
    else:
        A.symmetric_difference_update(b)

print(sum(A))

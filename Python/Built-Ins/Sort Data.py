N, M = map(int, input().split())

xs = [list(map(int, input().split()))for _ in range(N)]

K = int(input())

xs = sorted(xs, key=lambda x: x[K])

for i in xs:
    print(*i)

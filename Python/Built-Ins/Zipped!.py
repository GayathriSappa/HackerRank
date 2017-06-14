N, X = map(int, input().split())
[print(sum(j)/X) for j in zip(*[[float(i) for i in input().split()]for _ in range(X)])]

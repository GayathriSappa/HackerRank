M = int(input())
a = {int(i) for i in input().split()}
N = int(input())
b = {int(i) for i in input().split()}
c = sorted(a.symmetric_difference(b))
[print(i) for i in c]

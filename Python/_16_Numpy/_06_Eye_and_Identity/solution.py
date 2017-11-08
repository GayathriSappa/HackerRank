import numpy


n, m = map(int, input().split())
arr = numpy.eye(n, m, k=0)
print(arr)

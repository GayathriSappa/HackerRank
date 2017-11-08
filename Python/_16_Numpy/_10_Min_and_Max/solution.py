import numpy


n, m = map(int, input().split())
arr = numpy.array([list(map(int, input().split())) for _ in range(n)])
arr = numpy.min(arr, axis=1)
arr = numpy.max(arr)
print(arr)

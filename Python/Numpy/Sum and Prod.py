import numpy


n, m = map(int, input().split())
arr = numpy.array([list(map(int, input().split())) for _ in range(n)])
arr = numpy.sum(arr, axis=0)
arr = numpy.prod(arr)
print(arr)

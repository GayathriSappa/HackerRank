import numpy


n = int(input())
arr = numpy.array([list(map(float, input().split())) for _ in range(n)])
arr = numpy.linalg.det(arr)
print(arr)

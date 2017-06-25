import numpy


n = int(input())
arr1 = numpy.array([list(map(int, input().split())) for _ in range(n)])
arr2 = numpy.array([list(map(int, input().split())) for _ in range(n)])
arr = numpy.dot(arr1, arr2)
print(arr)

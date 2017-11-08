import numpy


n, m = map(int, input().split())
arr = numpy.array([list(map(int, input().split())) for _ in range(n)])
arr1 = numpy.mean(arr, axis=1)
print(arr1)
arr2 = numpy.var(arr, axis=0)
print(arr2)
arr3 = numpy.std(arr)
print(arr3)

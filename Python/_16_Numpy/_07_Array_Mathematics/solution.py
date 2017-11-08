import numpy


n, m = map(int, input().split())
arr1 = numpy.array([list(map(int, input().split())) for _ in range(n)])
arr2 = numpy.array([list(map(int, input().split())) for _ in range(n)])
arr = arr1 + arr2
print(arr)
arr = arr1 - arr2
print(arr)
arr = arr1 * arr2
print(arr)
arr = arr1 // arr2
print(arr)
arr = arr1 % arr2
print(arr)
arr = arr1 ** arr2
print(arr)

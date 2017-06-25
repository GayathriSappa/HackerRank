import numpy


arr1 = numpy.array(list(map(int, input().split())))
arr2 = numpy.array(list(map(int, input().split())))
arr = numpy.inner(arr1, arr2)
print(arr)
arr = numpy.outer(arr1, arr2)
print(arr)

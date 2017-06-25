import numpy


arr = numpy.array(list(map(float, input().split())))
arr1 = numpy.floor(arr)
print(arr1)
arr2 = numpy.ceil(arr)
print(arr2)
arr3 = numpy.rint(arr)
print(arr3)

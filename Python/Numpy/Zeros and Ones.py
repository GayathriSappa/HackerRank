import numpy


args = tuple(map(int, input().split()))

arr = numpy.zeros(args, dtype = numpy.int) 
print(arr)
arr = numpy.ones(args, dtype = numpy.int) 
print(arr)

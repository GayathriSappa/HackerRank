import numpy


arr = map(int, input().strip().split(' '))
d2_arr = numpy.array(list(arr))
d2_arr.shape = (3, 3)
print(d2_arr)

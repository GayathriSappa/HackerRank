import numpy


n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

arr = numpy.array(arr)
print(numpy.transpose(arr))
print(arr.flatten())

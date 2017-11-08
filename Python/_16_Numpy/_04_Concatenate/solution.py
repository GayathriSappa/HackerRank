import numpy


n, m, p = map(int, input().split())

arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(m)]

arr = numpy.concatenate((arr1, arr2), axis = 0)
print(arr)   

def binary_search(a, x):
    n = len(a)
    l = -1
    r = n
    while r > l + 1:
        m = (r + l) // 2
        if a[m] < x:
            l = m
        else:
            r = m
    if r < n and a[r] == x:
        return r
    else:
        return -1


v = int(input())
n = int(input())
ar = [int(i) for i in input().split()]

print(binary_search(ar, v))

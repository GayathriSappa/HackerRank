from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    d = deque([int(i) for i in input().split()])
    s = [float('inf')]

    while d:
        if len(d) == 1:
            i = d.pop()
            s.append(i)
        elif s[-1] >= d[0] >= d[-1]:
            i = d.popleft()
            s.append(i)
        elif s[-1] >= d[-1] > d[0]:
            i = d.pop()
            s.append(i)
        else:
            break

    print('Yes' if len(d) == 0 else 'No')

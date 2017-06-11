from collections import deque

N = int(input())
d = deque()
i = 0
while i < N:
    command = input().split()
    if command[0] == 'append':
        d.append(command[1])
    elif command[0] == 'appendleft':
        d.appendleft(command[1])
    elif command[0] == 'pop':
        d.pop()
    else:
        d.popleft()
    i += 1

[print(i, end=' ') for i in d]

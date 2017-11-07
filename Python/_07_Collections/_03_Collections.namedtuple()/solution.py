from collections import namedtuple


N = int(input())
column = input().split()
Student = namedtuple('Student', field_names=column)
s = 0
for i in range(N):
    a = Student(*input().split())
    s += int(a.MARKS)

print('%.2f' % (s/N))

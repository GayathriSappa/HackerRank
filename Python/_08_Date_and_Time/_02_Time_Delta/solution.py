from datetime import datetime, timedelta


T = int(input())
for _ in range(T):
    t1 = input()
    t2 = input()
    d1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    d2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    print('%d' % (abs(timedelta.total_seconds(d1-d2))))

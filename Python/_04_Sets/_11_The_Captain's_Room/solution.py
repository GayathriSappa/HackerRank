K = int(input())
xs = map(int, input().split())
total = dict()

for i in xs:
    if i not in total:
        total[i] = 1
    else:
        total[i] += 1

for k, v in sorted(total.items(), key=lambda x: x[1]):
    print(k)
    break

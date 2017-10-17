n = int(input())

count = 0
count_per_day = 5

for i in range(n):
    count_per_day //= 2
    count += count_per_day
    count_per_day *= 3

print(count)

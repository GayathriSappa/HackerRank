N = int(input())
xs = list(map(int, input().split()))

print(all((all([True if i > 0 else False for i in xs]), any([str(i) == str(i)[::-1] for i in xs]))))

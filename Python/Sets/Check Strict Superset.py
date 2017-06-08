A = set(map(int, input().split()))

print('False') if False in [(A.issuperset(set(map(int, input().split())))) for i in range(int(input()))] else print('True')

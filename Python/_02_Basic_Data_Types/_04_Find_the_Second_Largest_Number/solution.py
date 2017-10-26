if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    total = list()
    [total.append(i) for i in arr if i not in total]
    total.sort()
    print(total[-2])    


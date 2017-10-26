if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        command = input().split()
        if command[0] in 'insert':
            lst.insert(int(command[1]), int(command[2]))
        elif command[0] in 'print':
            print(lst)
        elif command[0] in 'remove':
            lst.remove(int(command[1]))
        elif command[0] in 'append':
            lst.append(int(command[1]))
        elif command[0] in 'sort':
            lst.sort()
        elif command[0] in 'pop':
            lst.pop()
        else:
            lst.reverse()

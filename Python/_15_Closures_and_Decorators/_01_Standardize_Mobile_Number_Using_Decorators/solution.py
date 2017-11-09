def wrapper(f):
    def fun(l):
        # complete the function
        temp = []
        for phone in l:
            x = len(phone)
            new_phone = '+91 ' + phone[x-10:x-5] + ' ' + phone[x-5:x]
            temp.append(new_phone)
        f(temp)
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)


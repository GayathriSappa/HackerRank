def print_formatted(number):
    # your code goes here
    n = len(bin(number))-2
    for i in range(1, number + 1):
        d = str(i)
        o = oct(i)
        h = hex(i)
        b = bin(i)
        print(d.rjust(n, ' '), o[2:].rjust(n, ' '), h[2:].upper().rjust(n, ' '), b[2:].rjust(n, ' ')) 

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

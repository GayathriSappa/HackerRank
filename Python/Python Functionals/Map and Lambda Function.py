cube = lambda x: pow(x, 3) # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    def fib():
        fib_list = []
        a, b = 0, 1
        while a < 1000:
            fib_list.append(a)
            a, b = b, a + b
        return fib_list
    fib_list = fib()
    return fib_list[:n]
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

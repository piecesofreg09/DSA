# Uses python3
def calc_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        temp = [0, 1]
        for i in range(2, n + 1):
            sm = temp[0] + temp[1]
            temp = [temp[1], sm]
        return sm


n = int(input())
print(calc_fib(n))

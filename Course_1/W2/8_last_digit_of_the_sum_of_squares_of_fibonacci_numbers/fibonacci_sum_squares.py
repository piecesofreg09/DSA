# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def fibonacci_sum_squares(n):
    m = 10
    period = [0, 1]
    pre, cur = 0, 1
    pre, cur = cur % m, (pre + cur) % m
    while not ((pre == period[0]) and (cur == period[1])):
        period.append(cur)
        pre, cur = cur % m, (pre + cur) % m
    period = period[:-1]
    
    rem1 = n % len(period)
    d1 = period[rem1]
    
    rem2 = (n + 1) % len(period)
    d2 = period[rem2]

    return (d1 * d2) % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares(n))
    #print(fibonacci_sum_squares_naive(n))

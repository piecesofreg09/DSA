# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fibonacci_sum(n):
    m = 10
    period = [0, 1]
    pre, cur = 0, 1
    pre, cur = cur % m, (pre + cur) % m
    while not ((pre == period[0]) and (cur == period[1])):
        period.append(cur)
        pre, cur = cur % m, (pre + cur) % m
    period = period[:-1]
    
    div = int(n / len(period))
    rem = n % len(period)
    
    summ = div * sum(period) + sum(period[:(rem+1)])

    return summ % 10
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))

# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

def fibonacci_partial_sum(from_, to):
    m = 10
    period = [0, 1]
    pre, cur = 0, 1
    pre, cur = cur % m, (pre + cur) % m
    while not ((pre == period[0]) and (cur == period[1])):
        period.append(cur)
        pre, cur = cur % m, (pre + cur) % m
    period = period[:-1]
    
    n = from_ - 1
    div = int(n / len(period))
    rem = n % len(period)
    
    summ1 = div * sum(period) + sum(period[:(rem+1)])
    
    n = to
    div = int(n / len(period))
    rem = n % len(period)
    
    summ2 = div * sum(period) + sum(period[:(rem+1)])
    
    return (summ2 - summ1) % 10
    
if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
    #print(fibonacci_partial_sum_naive(from_, to))
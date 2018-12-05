# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m
    
def get_fibonacci_huge(n, m):
    period = [0, 1]
    pre, cur = 0, 1
    pre, cur = cur % m, (pre + cur) % m
    while not ((pre == period[0]) and (cur == period[1])):
        period.append(cur)
        pre, cur = cur % m, (pre + cur) % m
    period = period[:-1]
    
    rem = n % len(period)
    
    return period[rem]

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))

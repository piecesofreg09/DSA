# Uses python3
import sys
import copy

def lcm_naive(a, b):
    a_b, b_b = copy.deepcopy(a), copy.deepcopy(b)
    while b != 0:
        a, b = b, a % b

    return int(a_b * b_b // a)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))


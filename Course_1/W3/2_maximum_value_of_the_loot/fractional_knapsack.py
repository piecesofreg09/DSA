# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    ratio = [(values[i] / weights[i], values[i], weights[i]) for i in range(len(weights))]
    ratio.sort(key=lambda x:x[0])
    while capacity > 0 and len(ratio) > 0:
        # get the largest density item
        pair = ratio.pop()
        # if the capacity fits the whole item or not
        if pair[2] <= capacity:
            value += pair[1]
            capacity -= pair[2]
        else:
            value += pair[1] * capacity / pair[2]
            capacity = 0

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

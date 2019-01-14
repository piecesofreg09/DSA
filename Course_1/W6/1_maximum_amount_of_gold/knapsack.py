# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    value = [[0 for i in range(len(w) + 1)] for i in range(W + 1)]
    
    for i in range(1, len(w) + 1):
        for weight in range(1, W + 1):
            value[weight][i] = value[weight][i - 1]
            if w[i - 1] <= weight:
                val = value[weight - w[i - 1]][i - 1] + w[i - 1]
                if val > value[weight][i]:
                    value[weight][i] = val
    
    return value[W][len(w)]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

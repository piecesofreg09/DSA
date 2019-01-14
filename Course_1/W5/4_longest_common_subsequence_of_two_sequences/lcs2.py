#Uses python3

import sys

def lcs2(s, t):
    #write your code here
    D = [[0 for i in range(len(t) + 1)] for j in range(len(s) + 1)]
    
    for j in range(1, len(t) + 1):
        for i in range(1, len(s) + 1):
            insertion = D[i][j - 1]
            deletion = D[i - 1][j]
            match = D[i - 1][j - 1] + 1
            mismatch = D[i - 1][j - 1]
            if s[i - 1] == t[j - 1]:
                D[i][j] = max(insertion, deletion, match)
            else:
                D[i][j] = max(insertion, deletion, mismatch)
    return D[len(s)][len(t)]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))

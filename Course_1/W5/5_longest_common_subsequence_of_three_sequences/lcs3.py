#Uses python3

import sys

def lcs3(s, t, u):
    #write your code here
    D = [[[0 for k in range(len(u) + 1)] for i in range(len(t) + 1)] for j in range(len(s) + 1)]
    
    for k in range(1, len(u) + 1):
        for j in range(1, len(t) + 1):
            for i in range(1, len(s) + 1):
                #print(D[i][j - 1][k - 1])
                insertion_x = D[i - 1][j][k]
                #print(D[i - 1][j][k - 1])
                insertion_y = D[i][j - 1][k]
                #print(D[i - 1][j - 1][k])
                insertion_z = D[i][j][k - 1]
                
                match = D[i - 1][j - 1][k - 1] + 1
                mismatch = D[i - 1][j - 1][k - 1]
                
                if s[i - 1] == t[j - 1] and s[i - 1] == u[k - 1]:
                    D[i][j][k] = max(insertion_x, insertion_y, insertion_z, match)
                else:
                    D[i][j][k] = max(insertion_x, insertion_y, insertion_z, mismatch)
    return D[len(s)][len(t)][len(u)]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))

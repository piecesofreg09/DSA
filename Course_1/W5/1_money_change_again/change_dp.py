# Uses python3
import sys

def get_change(m):
    #write your code here
    
    if m < 4:
        res = [1, 2, 1, 1]
        return res[m - 1]
    else:
        res = [0] * m
        res[0:4] = [1, 2, 1, 1]
        for i in range(4, m):
            res[i] = min(1 + res[i - 1], 1 + res[i - 3], 
                1 + res[i - 4])
    
    return res[m - 1]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

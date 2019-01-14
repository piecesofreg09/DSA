# Uses python3
import sys

def optimal_summands(n):
    summands = []
    
    last = 1
    while n > 0:
        if (n - last) <= last:
            last = n
            n -= last
            summands.append(last)
        else:
            n -= last
            summands.append(last)
            last += 1
        
            
    
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

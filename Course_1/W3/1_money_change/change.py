# Uses python3
import sys

def get_change(m):
    rem = m
    n10 = rem // 10
    rem = rem % 10
    
    n5 = rem // 5
    rem = rem % 5
    
    n1 = rem // 1
    
    return (n10 + n5 + n1)

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

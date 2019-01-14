# Uses python3
import sys
import random

def binary_search_det(a, key, low, high):
    if high < low:
        return - 1
    mid = low + (high - low) // 2
    if key == a[mid]:
        return mid
    elif key < a[mid]:
        return binary_search_det(a, key, low, mid - 1)
    else:
        return binary_search_det(a, key, mid + 1, high)

def binary_search(a, x):
    left, right = 0, len(a) - 1
    # write your code here
    
    return binary_search_det(a, x, left, right)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    
    m = data[n + 1]
    a = data[1 : n + 1]
    
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
    
    
    '''
    a = sorted([random.randrange(0, 900000) for i in range(n)])
    xlist = [random.randrange(0, 900000) for i in range(10000)]
    
    res1 = []
    for x in xlist:
        # replace with the call to binary_search when implemented
        res1.append(binary_search(a, x))
    print()
    res2 = []
    for x in xlist:
        # replace with the call to binary_search when implemented
        res2.append(linear_search(a, x))
    sub = []
    for i in range(len(xlist)):
        sub.append(abs(res1[i] - res2[i]))
    print(max(sub))
    '''
# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    x = a[l]
    same = l
    j = l
    #print('origi')
    #print(a)
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
        elif a[i] == x:
            same += 1
            j += 1
            a[same], a[i] = a[i], a[same]
            if same != j:
                a[j], a[i] = a[i], a[j]
        #print(a)
        #print('same = ' + str(same) + 'j = ' + str(j))
    a[(j - same + l):(j + 1)], a[l:(l + j - same)] = a[l:(same + 1)], a[(same + 1):(j + 1)]
    #print('at last')
    #print(a)
    return (l + j - same, j)
            
    

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
        print(a)
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    (m, n) = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1)
    randomized_quick_sort(a, n + 1, r)


if __name__ == '__main__':
    
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
    
    '''
    import random
    n = int(input().strip())
    a = [random.randrange(0, 900000) for i in range(n)]
    res = sorted(a)
    
    randomized_quick_sort(a, 0, n - 1)
    sub = [0] * len(a)
    for i in range(len(a)):
        sub[i] = abs(res[i] - a[i])
    print(max(sub))
    '''

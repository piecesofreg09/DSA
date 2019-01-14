# Uses python3
import sys
import math
sys.setrecursionlimit(100000)

def optimal_sequence_v1(n, res):
    #sequence = []
    #print(n)
    if n in res:
        return res[n]
    else:
        #sequence.append(n)
        n1, n2 = [float('Inf'), float('Inf')]
        n3 = [float('Inf')]
        n1_flag = False
        n2_flag = False
        minn3 = float('Inf')
        if n % 3 == 0:
            n1 = len(optimal_sequence(n // 3, res)) + 1
            n1_flag = True
        if n % 2 == 0:
            n2 = len(optimal_sequence(n // 2, res)) + 1
            n2_flag = True
        
        ending = max(n - 2, n // 3)
        if n1_flag and n2_flag:
            rng = list(range(n - 1, n // 2, -1)) + list(range(n // 2 - 1, ending, -1))
        else:
            rng = range(n - 1, ending, -1)
            
        #print(list(rng))
        n3 = [float('Inf')] * (n - 1 - n // 3)
        minn3 = float('Inf')
        minn3_id = -1
        for i in rng:
            n3[n - 1 - i] = len(optimal_sequence(i, res)) + (n - i)
            if n3[n - 1 - i] < minn3:
                minn3 = n3[n - 1 - i]
                minn3_id = i
        
        minn = min(n1, n2, minn3)
        #print('minn = ' + str(minn))
        if n1 == minn:
            res[n] = res[n // 3] + [n]
        elif n2 == minn:
            res[n] = res[n // 2] + [n]
        else:
            #print('minn3_id' + str(minn3_id))
            #print(res[minn3_id])
            res[n] = res[minn3_id] + list(range(minn3_id + 1, n + 1))
        return res[n]

def optimal_sequence(n):
    x = [None for i in range(max(4, n + 1))]
    x[0] = []
    x[1] = [1]
    x[2] = [1, 2]
    x[3] = [1, 3]
    for num in range(4, n + 1):
        n3 = float('Inf')
        n2 = float('Inf')
        if num % 3 == 0:
            n3 = len(x[num // 3]) + 1
        if num % 2 == 0:
            n2 = len(x[num // 2]) + 1
        n_1_1 = len(x[num - 1]) + 1
        n_1_2 = len(x[num - 2]) + 2
        n_1_3 = len(x[num - 3]) + 3
        minn = min(n3, n2, n_1_1, n_1_2, n_1_3)
        if minn == n3:
            x[num] = x[num // 3] + [num]
        elif minn == n2:
            x[num] = x[num // 2] + [num]
        elif minn == n_1_1:
            x[num] = x[num - 1] + [num]
        elif minn == n_1_1:
            x[num] = x[num - 2] + [num - 1, num]
        elif minn == n_1_1:
            x[num] = x[num - 3] + [num - 2, num - 1, num]
    return x[n]
        
input = sys.stdin.read()
n = int(input)
#res = {0:[], 1:[1], 2:[1, 2], 3:[1, 3]}
#print(len(optimal_sequence(n)) - 1)
#print(optimal_sequence(n))
#print(res)

sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

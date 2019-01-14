# Uses python3
import sys
import itertools

def partition3(A):
    summ = sum(A)
    if summ % 3 != 0:
        return False
    else:
        div_sum = summ // 3
        res = [[[False for i in range(len(A) + 1)] for j in range(div_sum + 1)] for k in range(div_sum + 1)]
        for i in range(len(A) + 1):
            res[0][0][i] = True
        #prefill items first
        for i in range(1, div_sum + 1):
            for k in range(1, len(A) + 1):
                t1 = res[i][0][k - 1]
                t2 = False
                if i >= A[k - 1]:
                    t2 = res[i - A[k - 1]][0][k - 1]
                res[i][0][k] = t1 or t2
        for j in range(1, div_sum + 1):
            for k in range(1, len(A) + 1):
                t1 = res[0][j][k - 1]
                t2 = False
                if j >= A[k - 1]:
                    t2 = res[0][j - A[k - 1]][k - 1]
                res[i][0][k] = t1 or t2
        for i in range(1, div_sum + 1):
            for j in range(1, div_sum + 1):
                for k in range(1, len(A) + 1):
                    t1 = res[i][j][k - 1]
                    
                    t2 = False
                    if i >= A[k - 1]:
                        t2 = res[i - A[k - 1]][j][k - 1]
                    
                    t3 = False
                    if j >= A[k - 1]:
                        t3 = res[i][j - A[k - 1]][k - 1]
                    
                    res[i][j][k] = t1 or t2 or t3
        #print(res)
        return res[div_sum][div_sum][len(A)]
        
def partition3_naive(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1
    return 0
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(int(partition3(A)))


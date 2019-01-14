# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    mid = left + (right - left) // 2
    
    left_maj = get_majority_element(a, left, mid)
    right_maj = get_majority_element(a, mid, right)
    
    if left_maj == right_maj:
        if left_maj ==  -1:
            return -1
        else:
            return left_maj
    else:
        left_maj_n = 0
        right_maj_n = 0
        for i in range(left, right):
            if a[i] == left_maj:
                left_maj_n += 1
            elif a[i] == right_maj:
                right_maj_n += 1
        
        if left_maj_n > (right - left) / 2:
            return left_maj
        elif right_maj_n > (right - left ) / 2:
            return right_maj
        else:
            return -1
    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

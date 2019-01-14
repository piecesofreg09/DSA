# Uses python3
import sys

# right is exclusive
def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    j = ave
    #print(a)
    #print('left=' + str(left))
    #print('ave=' + str(ave))
    #print('right=' + str(right))
    #print(range(left, ave))
    for i in range(left, ave):
        #print('i = ' + str(i) + ' j = ' + str(j))
        while ((j < right) and (a[i] > a[j])):
            j += 1
        #print('j=' + str(j))
        #print(j - ave)
        number_of_inversions += (j - ave)
    t = []
    j = ave
    #print('leftave=' + str(a[left:ave]))
    #print('averight=' + str(a[ave:right]))
    for i in range(left, ave):
        while ((j < right) and (a[i] > a[j])):
            t.append(a[j])
            j += 1
        t.append(a[i])
    t.extend(a[j:right])
    #print(t)
    a[left:right] = t
            
    return number_of_inversions
def get_number_of_inversions_naive(a, b, left, right):
    res = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                res += 1
    return res
    
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    #print(a)
    #print(b)
    #print(get_number_of_inversions_naive(a, b, 0, len(a)))
    print(get_number_of_inversions(a, b, 0, len(a)))
    

#Uses python3

import sys

def IsGreaterOrEqual(digit, maxDigit):
    if maxDigit == - float('Inf'):
        return digit
    else:
        v1 = int(str(digit) + str(maxDigit))
        v2 = int(str(maxDigit) + str(digit))
        if v1 > v2:
            return True
        else:
            return False
                
        

def largest_number(a):
    #write your code here
    res = ""
    
    while len(a) > 0:
        maxDigit = - float('Inf')
        maxDigitInd = - float('Inf')
        for id, digit in list(enumerate(a)):
            if IsGreaterOrEqual(digit, maxDigit):
                maxDigit = digit
                maxDigitInd = id
        next = a.pop(maxDigitInd)
        res += next
    
    
    
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    

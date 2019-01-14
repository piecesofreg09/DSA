# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

        
def MinAndMax(digits, operators, m, M, i, j):
    minv = float('Inf')
    maxv = -float('Inf')
    
    for k in range(i, j):
        a = evalt(M[i][k], M[k + 1][j], operators[k])
        b = evalt(M[i][k], m[k + 1][j], operators[k])
        c = evalt(m[i][k], M[k + 1][j], operators[k])
        d = evalt(m[i][k], m[k + 1][j], operators[k])
        minv = min(minv, a, b, c, d)
        maxv = max(maxv, a, b, c, d)
    return (minv, maxv)
        
def get_maximum_value(dataset):
    #write your code here
    lange = len(dataset)
    digits = [v for i, v in enumerate(dataset) if i % 2 == 0]
    operators = [v for i, v in enumerate(dataset) if i % 2 != 0]
    M = [[0 for i in range(len(digits))] for j in range(len(digits))]
    m = [[0 for i in range(len(digits))] for j in range(len(digits))]
    for i in range(len(digits)):
        m[i][i] = int(digits[i])
        M[i][i] = int(digits[i])
    for s in range(1, len(digits)):
        for i in range(len(digits) - s):
            j = i + s
            m[i][j], M[i][j] =  MinAndMax(digits, operators, m, M, i, j)
    #print(m)
    #print(M)
    return M[0][len(digits) - 1]


if __name__ == "__main__":
    print(get_maximum_value(input()))

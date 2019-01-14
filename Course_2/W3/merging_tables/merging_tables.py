# python3

import sys


n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))

'''
with open('./tests/116', 'r') as inputt:
    n, m = map(int, inputt.readline().split())
    lines = list(map(int, inputt.readline().split()))
    dess = [0 for _ in range(m)]
    sous = [0 for _ in range(m)]
    for i in range(m):
        dess[i], sous[i] = map(int, inputt.readline().split())
'''
rank = [1] * n
parent = list(range(0, n))
real_parent = list(range(0, n))
ans = max(lines)

def getParent(table):
    # find parent and compress path
    if table != parent[table]:
        parent[table] = getParent(parent[table])

    return parent[table]

def merge(destination, source):
    global ans
    realDestination, realSource = getParent(destination), getParent(source)
    #print('real des' + str(realDestination))
    #print('real sou' + str(realSource))
    if realDestination == realSource:
        return False

    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size

    if rank[realDestination] > rank[realSource]:
        parent[realSource] = realDestination
        lines[realDestination] += lines[realSource]
        lines[realSource] = 0
    else:
        parent[realDestination] = realSource
        lines[realSource] += lines[realDestination]
        lines[realDestination] = 0
        if rank[realDestination] == rank[realSource]:
            rank[realSource] += 1
    #print(rank)
    #print(lines)
    #print(parent)
    ans = max(ans, lines[realSource], lines[realDestination])
    return ans

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans)

'''
with open('./116.aaaa', 'w+') as outputt, open('./tests/116.a', 'r') as answers:
    for i in range(m):
        destination, source = dess[i], sous[i]
        merge(destination - 1, source - 1)
        #print(ans)
        outputt.write(str(ans) + '\n')
        cor_ans = int(answers.readline())
        if abs(ans - cor_ans) > 1e-3:
            print('Wrong at line ' + str(i))
'''

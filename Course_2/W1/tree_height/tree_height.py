# python3

import sys
import threading

class Node:
    def __init__(self):
        self.children = []
    def addChild(self, child):
        self.children.append(child)
    
    def height(self):
        if len(self.children) == 0:
            return 1
        else:
            temp = []
            for child in self.children:
                temp.append(child.height())
            return 1 + max(temp)
        

def compute_height_naive(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height

def compute_height(n, parents):
    nodes = [Node() for i in range(n)]
    for vertex in range(n):
        pi = parents[vertex]
        if pi == -1:
            root = nodes[vertex]
        else:
            nodes[pi].addChild(nodes[vertex])
    #for vertex in range(n):
    #    print(nodes[vertex].children)
    #    print(nodes[vertex].height())
    return root.height()
    

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))
    #print(compute_height_naive(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

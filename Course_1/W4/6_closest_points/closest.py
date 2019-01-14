#Uses python3
import sys
import math
#import random
#import time

def minimum_distance_naive(x, y):
    d_min = float('Inf')
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            t = (x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j])
            d_min = min(t, d_min)
    return d_min

def binary_left(x, low, high, mid_point, d):
    # high is exclusive
    if high - low == 1:
        return low
    mid = low + (high - low) // 2
    if mid_point - x[mid] > d:
        return binary_left(x, mid, high, med, d)
    else:
        if mid == low or (mid_point - x[mid - 1]) > d:
            return mid
        else:
            return binary_left(x, low, mid, mid_point, d)
            

def minimum_distance(x, y):
    #write your code here
    if len(x) == 1:
        return float('Inf')
    elif len(x) == 2:
        xd = x[0] - x[1]
        yd = y[0] - y[1]
        return xd * xd + yd * yd
    else:
        med = len(x) // 2
        d1 = minimum_distance(x[:med], y[:med])
        d2 = minimum_distance(x[med:], y[med:])
        d = min(d1, d2)
        
        mid_point = (x[med - 1] + x[med]) / 2
        
        i = med - 1
        while i > -1 and (mid_point - x[i]) <= math.sqrt(d):
            i -= 1
        
        j = med
        while j < len(x) and (x[j] - mid_point) <= math.sqrt(d):
            j += 1
        
        #print(str(i) + ' ' + str(med) + ' ' + str(j))
        temp2sort = list(zip(x[(i + 1):j], y[(i + 1):j]))
        temp2sort.sort(key=lambda cor: cor[1])
        d_min_temp = float('Inf')
        if len(temp2sort) > 0:
            x_temp, y_temp = list(zip(*temp2sort))
            
            for y_i in range(0, len(x_temp)):
                for y_i_seven in range(y_i + 1, min(y_i + 8, len(x_temp))):
                    xd = x_temp[y_i] - x_temp[y_i_seven]
                    yd = y_temp[y_i] - y_temp[y_i_seven]
                    t = (xd) * (xd) + (yd) * (yd)
                    d_min_temp = min(t, d_min_temp)
        
        return min(d, d_min_temp)
    

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    
    x = data[1::2]
    y = data[2::2]
    
    sorted_res = sorted(list(zip(x, y)), key=lambda x: (x[0], x[1]))
    x, y = zip(*sorted_res)
    x = list(x)
    y = list(y)
    
    print("{0:.15f}".format(math.sqrt(minimum_distance(x, y))))
    
    
    '''
    #x = [random.randrange(-100000, 900000) for i in range(n)]
    for rpt in range(50):
        x = [0] * n
        x = [random.randrange(-100, 100) for i in range(n)]
        y = [random.randrange(-100, 100) for i in range(n)]
        
        
        t1 = time.time()
        
        sorted_res = sorted(list(zip(x, y)), key=lambda x: (x[0], x[1]))
        x, y = zip(*sorted_res)
        x = list(x)
        y = list(y)
        #print(time.time() - t1)
        
        
        t2 = time.time()
        res1 = math.sqrt(minimum_distance(x, y))
        #print("{0:.9f}".format(res1))
        #print(time.time() - t2)
        
        
        t3 = time.time()
        res2 = math.sqrt(minimum_distance_naive(x, y))
        #print("{0:.9f}".format(res2))
        #print(time.time() - t3)
        
        if abs(res1 - res2) > 1e-6:
            print('Not Pass in case ' + str(i))
        else:
            print('Pass')
    '''
    
    # test for constant
    '''
    for n in [1000, 2000, 3000, 5000, 8000, 10000, 20000, 40000, 80000, 100000]:
        t = []
        sz = 5
        for ttt in range(sz):
        
            x = [random.randrange(-1000000000, 1000000000) for i in range(n)]
            y = [random.randrange(-1000000000, 1000000000) for i in range(n)]
            
            
            t1 = time.time()
            
            sorted_res = sorted(list(zip(x, y)), key=lambda x: (x[0], x[1]))
            x, y = zip(*sorted_res)
            x = list(x)
            y = list(y)
            #print(time.time() - t1)
            
            
            t2 = time.time()
            print("{0:.9f}".format(math.sqrt(minimum_distance(x, y))))
            t.append(time.time() - t2)
        print('constant is')
        print(sum(t) / sz / n / math.log(n) / math.log(n))
        
        
        #t3 = time.time()
        #print("{0:.9f}".format(math.sqrt(minimum_distance_naive(x, y))))
        #print(time.time() - t3)
    '''
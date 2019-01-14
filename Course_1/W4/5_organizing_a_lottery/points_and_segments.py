# Uses python3
import sys
#import random
#import time
#import copy

def binary_search_start(points, s, l, r):
    
    med = (l + r) // 2
    if s == points[med]:
        return med
    else:
        if (r - l) ==  1:
            return r
        if s < points[med]:
            return binary_search_start(points, s, l, med)
        else:
            return binary_search_start(points, s, med, r)
    
def binary_search_end(points, e, l, r):
    
    med = (l + r) // 2
    if e == points[med]:
        return med + 1
    else:
        if (r - l) == 1:
            return r
        if e < points[med]:
            return binary_search_end(points, e, l, med)
        else:
            return binary_search_end(points, e, med, r)
    

def fast_count_segments_v1(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    
    
    
    points_id = sorted(range(len(points)), key=points.__getitem__)
    #print(points_id)
    points.sort()
    
    
    #print(points)
    i = 0
    uni_points = []
    aug_points = []
    while i < len(points):
        j = 1
        while (i + j) < len(points) and points[i + j] == points[i]:
            j += 1
        uni_points.append(points[i])
        aug_points.append(j)
        i += j
    
    #print(uni_points)
    #print(aug_points)
    
    uni_points = [-float('Inf')] + uni_points
    uni_points.append(float('Inf'))
    
    for i in range(len(starts)):
        start_id = binary_search_start(uni_points, starts[i], 0, len(uni_points)) - 1
        end_id = binary_search_end(uni_points, ends[i], 0, len(uni_points)) - 1
        #print('start ' + str(starts[i]) + ' end ' + str(ends[i])) 
        #print('start_id = ' + str(start_id) + ' end_id = ' + str(end_id))
        cnt[start_id:end_id] = list(map(lambda x: x + 1, cnt[start_id:end_id]))
        #print(cnt)
    
    cnt_full = []
    for i in range(len(uni_points) - 2):
        cnt_full.extend([cnt[i]] * aug_points[i])
    res = [0] * len(points)
    for id, i in enumerate(points_id):
        res[i] = cnt_full[id]
    
    return res

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                #print('seg ' + str(starts[j]) + ' ' + str(ends[j]) + ' value ' + str(points[i]))
                cnt[i] += 1
    return cnt

def fast_count_segments(starts, ends, points):
    
    cnt = [0] * len(points)
    
    #print(points)
    
    starts_zip = list(zip(starts, [1] * len(starts)))
    ends_zip = list(zip(ends, [-1] * len(ends)))
    points_zip = list(zip(points, [0] * len(points), list(range(len(points)))))
    #print(points_zip)
    full = starts_zip + ends_zip + points_zip
    
    full.sort(key=lambda x: (x[0], -x[1]))
    
    #print(full)
    
    res = 0
    for x in full:
        res += x[1]
        if len(x) == 3:
            cnt[x[2]] = res
    return cnt
    
    
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    
    
    cnt_f = fast_count_segments(starts, ends, points)
    for x in cnt_f:
        print(x, end=' ')
    
    #use fast_count_segments
    
    '''
    #random input trial
    starts = [random.randrange(-10, 90) for i in range(n)]
    ends = [starts[i] + random.randrange(0, 90) for i in range(n)]
    points = [random.randrange(-10, 90) for i in range(n)]
    
    
    points_copy = copy.deepcopy(points)
    t1 = time.time()
    cnt_n = naive_count_segments(starts, ends, points)
    print(time.time() - t1)
    #for x in cnt_n:
        #print(x, end=' ')
    print()
    
    t2 = time.time()
    
    cnt_f = fast_count_segments_v1(starts, ends, points)
    print(time.time() - t2)
    #for x in cnt_f:
        #print(x, end=' ')
    print()
    
    
    t3 = time.time()
    cnt_ff = fast_count_segments(starts, ends, points_copy)
    print(time.time() - t3)
    #for x in cnt_ff:
        #print(x, end=' ')
    
    
    #compare the difference between naive and fast
    sub = [abs(a - b) for a, b in zip(cnt_n, cnt_f)]
    print()
    print(max(sub))
    
    sub = [abs(a - b) for a, b in zip(cnt_n, cnt_ff)]
    print()
    print(max(sub))
    '''

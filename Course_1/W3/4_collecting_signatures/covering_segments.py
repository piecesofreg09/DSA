# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    segments.sort(key=lambda seg: seg.end)
    
            
    fe = segments.pop(0)
    while len(segments) > 0:
        points.append(fe.end)
        fe = segments.pop(0)
        while fe.start <= points[-1] and len(segments) > 0:
            fe = segments.pop(0)
    
    if fe.start > points[-1]:
        points.append(fe.end)
        
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')

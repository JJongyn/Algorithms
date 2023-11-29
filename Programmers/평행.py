'''
https://school.programmers.co.kr/learn/courses/30/lessons/120875
'''

from itertools import permutations

def solution(dots):
    
    a, b, c, d = dots[0], dots[1], dots[2], dots[3]
    # case 1: 0, 1
    delta_12 = abs((a[1] - b[1]) / (a[0]-b[0]))
    delta_34 = abs((c[1] - d[1]) / (c[0]-d[0]))
    
    # case 2: 0, 2
    delta_13 = abs((a[1] - c[1]) / (a[0]-c[0]))
    delta_24 = abs((b[1] - d[1]) / (b[0]-d[0]))
    
    # case 3: 0, 3
    delta_14 = abs((a[1] - d[1]) / (a[0]-d[0]))
    delta_23 = abs((b[1] - c[1]) / (b[0]-c[0]))
    
    if delta_12 == delta_34 or delta_13==delta_24 or delta_14==delta_23:
        return 1
    
    return 0
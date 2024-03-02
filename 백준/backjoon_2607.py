'''
실버2. https://www.acmicpc.net/problem/2607
'''

import sys
import copy

input = sys.stdin.readline

N = int(input().rstrip())

data = [input().rstrip() for _ in range(N)]
target = data[0]
target = sorted(list(target))

total = 0
for item in data[1:]:
    ex_cnt = 0
    item = sorted(list(item))
    item_cp = copy.deepcopy(item)
    for t in target:
        if t in item_cp:
            item_cp.remove(t)
        else:
            ex_cnt += 1
    
    if ex_cnt < 2 and len(item_cp) <= 1:
        total += 1
            
print(total)
        
    

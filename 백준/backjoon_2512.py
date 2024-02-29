'''
실버2. https://www.acmicpc.net/problem/2512
'''

import sys

input = sys.stdin.readline

N = int(input())
call_list = list(map(int, input().split()))
total = int(input())


def return_sum(data, target):
    return sum([d if d <= target else target for d in data])
        

answer = 0
if sum(call_list) <= total:
    answer = max(call_list)
else:
    start = 0
    end = max(call_list)
    
    while start <= end:
        mid = (start + end) // 2
        
        if return_sum(call_list, mid) == total:
            answer = max(mid, answer)
            break
        elif return_sum(call_list, mid) < total:
            answer = max(mid, answer)
            start = mid + 1
        else:
            end = mid - 1
            
print(answer)
    




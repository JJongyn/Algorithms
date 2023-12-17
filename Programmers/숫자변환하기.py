'''
LV2. https://school.programmers.co.kr/learn/courses/30/lessons/154538

'''

from collections import deque

def solution(x, y, n):
    
    queue = deque([(y, 0)])
    
    while queue:
        current, cnt = queue.popleft()
        if current == x:
            return cnt
        
        if current > x:
            cnt += 1

            if current % 3 == 0:
                queue.append([current // 3, cnt])
            if current % 2 == 0:
                queue.append([current // 2, cnt])

            queue.append([current - n, cnt])
    
    return -1
    
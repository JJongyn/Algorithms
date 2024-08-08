'''
https://www.acmicpc.net/problem/2877

4 or 7로 이루어진 가장 작은 수
'''


import sys
from collections import deque

input = sys.stdin.readline

K = int(input())

cnt = 0
q = deque(['4', '7'])

while q:
    current_num = q.popleft()
    cnt += 1
    if cnt == K:
        print(current_num)
        break
    q.append(current_num + '4')
    q.append(current_num + '7')
    

    

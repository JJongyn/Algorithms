'''
실버3. https://www.acmicpc.net/problem/1515

stack에 넣고 빼면서 stack이 비었을 떄의 값을 출력

3000 * 3000 = 9000000
'''
import sys
from collections import deque

input = sys.stdin.readline
M = deque(input().rstrip())

i = 0
while True:
    i += 1
    for j in str(i):
        if M and M[0] == j:
            M.popleft()
    
    if not M:
        print(i)
        break
import sys
from collections import deque

input = sys.stdin.readline

target = int(input())
M = int(input())

data = []
if M  > 0:
    data = list(map(int ,input().split()))

current = 100

ans = abs(target - current) # +랑 -로만 이동하는 경우의 수

for i in range(1000001):
    num = str(i)
    
    for j in range(len(num)):
        if int(num[j]) in data:
            break
    
    else:
        ans = min(len(num) + abs(target-int(num)), ans)
        
print(ans)
    
    

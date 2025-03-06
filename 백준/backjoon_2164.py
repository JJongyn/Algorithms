import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
arr = deque([i for i in range(1, N+1)])

while len(arr) > 1:
    arr.popleft()
    arr.append(arr.popleft())
    
print(*arr)
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

data = [i for i in range(1, N+1)]
selected = list(map(int, sys.stdin.readline().split()))

deq = deque(data)
result = []
cnt = 0
while True:
    if len(result) == M:
        print(cnt)
        break
    else:    
        for i in selected:
            if deq.index(i) < len(deq) / 2:
               cnt += deq.index(i)
               deq.rotate(-deq.index(i))
               result.append(deq.popleft())
            else:
               cnt += len(deq) - deq.index(i) 
               deq.rotate(len(deq) - deq.index(i))
               result.append(deq.popleft())







        
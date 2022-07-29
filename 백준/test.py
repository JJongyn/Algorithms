import sys
from collections import deque

order = []

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
deq = deque(data)

print(deq)

deq.popleft()
deq.rotate(-3)
print(deq)

deq.rotate(1)
print(deq)
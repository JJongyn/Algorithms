import sys
from collections import deque

order = []

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
# enumerate 사용하면 index도 같이 저장할 수 있다!!!!
deq = deque(enumerate(data))


while(deq):
    idx, dump = deq.popleft()
    print(idx+1, end=' ')
    if (dump > 0) : dump = dump - 1 # pop 하고 이동하니깐
    deq.rotate(-dump)


import sys
from collections import deque

queue = deque([])
n, k = sys.stdin.readline().split()
data = []

for i in range(int(n)):
    queue.append(i+1)

cnt = 0
while(queue):

    for i in range(int(k)-1):    
        queue.append(queue.popleft())
    data.append(queue.popleft())

print("<", end="")
for i in range(len(data)-1):
    print("{0}".format(data[i]),end=", ")
print(data[-1], end=">")

    

    



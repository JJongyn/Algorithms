import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

visited = [0] * 100001
def search(x):
    queue = deque()
    queue.append(x)
    
    while queue:
        x = queue.popleft()
        
        if x == K:
            return visited[x]
        
        for nx in [x+1, x-1, x*2]:
            if 0 <= nx <= 100000 and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                queue.append(nx)
# search(N)
print(search(N))
                
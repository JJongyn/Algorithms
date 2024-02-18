'''
골드4. https://www.acmicpc.net/problem/14502
'''
from collections import deque
import copy

N, M = map(int, input().split())


graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0
def bfs():
    q = deque()
    new_graph = copy.deepcopy(graph)
    for i in range(N):
        for j in range(M):
            if new_graph[i][j] == 2:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                if new_graph[nx][ny] == 0:
                    new_graph[nx][ny] = 2
                    q.append((nx, ny))
                    
    global answer 
    cnt = 0
    
    for i in range(N):
        cnt += new_graph[i].count(0)
    
    answer = max(cnt, answer)
    

def make(cnt):

    if cnt == 3:
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make(cnt + 1)
                graph[i][j] = 0
make(0)
print(answer)
                
                        
    
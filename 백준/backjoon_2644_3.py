import sys

input = sys.stdin.readline

n = int(input()) # 전체 사람의 수
a, b = map(int, input().split()) 

m = int(input()) # 전체 사람의 수
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


answer = -1
# start가 x, end가 b
def search(x, cnt):
    global answer

    visited[x] = True

    if x == b:
        answer = cnt
        return answer

    for nx in graph[x]:
        if visited[nx] is False:
            search(nx, cnt+1)
    return answer

print(search(a, 0))
    


    

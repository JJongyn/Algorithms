import sys

n = int(sys.stdin.readline())
visited = [False] * (n+1) # 1부터 시작
conneted = int(sys.stdin.readline()) # 연결된 컴퓨터의 쌍


###### 그래프 구조를 만듬 ######
graph = [[] for i in range(n+1)] # 2차원으로 graph연결을 넣을 list
for i in range(conneted):
    a, b = map(int, input().split())
    graph[a].append(b) # a랑 b의 연결관계를 a에 넣음
    graph[b].append(a) # a랑 b의 연결관계를 b에도 넣어줌

count = 0

###### 여기는 기존의 dfs 방식 ######
def dfs(graph, v, visited):
    visited[v] = True
    global count 
    for i in graph[v]:
        if not visited[i]:
            count += 1
            dfs(graph, i, visited)

dfs(graph, 1, visited)
print(count)
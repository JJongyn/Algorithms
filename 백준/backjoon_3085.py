import sys
import copy

input = sys.stdin.readline

N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]

def check_max_length(graph, N, axis=0):
    best = 1
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            prev, curr = (graph[i][j-1], graph[i][j]) if axis == 0 else (graph[j-1][i], graph[j][i])
            cnt = cnt + 1 if prev == curr else 1
            best = max(best, cnt)
    return best

result = 1
for i in range(N):
    for j in range(N):
        if j + 1 < N:
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
            best = max(check_max_length(graph, N, axis=0), check_max_length(graph, N, axis=1))
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
            result = max(best, result)
        if i + 1 < N:
            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]
            best = max(check_max_length(graph, N, axis=0), check_max_length(graph, N, axis=1))
            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]
            result = max(best, result)
            
print(result)
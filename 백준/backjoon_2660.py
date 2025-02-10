import sys
from collections import deque


input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

'''
1    2         ===> 2, 3, 5                      가능 3개
2    1, 3, 4   ===> 2 -> 3 -> 5 / 2 -> 4 -> 5    가능 2개
3    2, 4, 5   ===> 3 -> 2 -> 1                  가능 2개
4    3, 5, 2   ===> 4 -> 2 -> 1                  가능 2개
5    4, 3      ===> 5 -> 3 -> 2 -> 1             가능 3개
'''

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)


def search(start, graph):
    q = deque()
    q.append(start)

    visited = [0] * (N+1)
    visited[start] = 1

    while q:
        current = q.popleft()
        for next in graph[current]: # 연결된 노드 들어가기
            if visited[next] == 0:
                visited[next] = visited[current] + 1
                q.append(next)

    # print(visited) # Max에서 1뺴야지 엣지니깐
    return max(visited) - 1

min_v = 100
results = [search(i + 1, graph) for i in range(N)]
min_v = min(results)

candidates = []
for i, result in enumerate(results):
    if result == min_v: candidates.append(str(i+1))

print(min_v, len(candidates))
print(' '.join(candidates))
        







'''
https://www.acmicpc.net/problem/5014
'''

import sys
from collections import deque


input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
visited = [0 for _ in range(F+1)]

def bfs(start, end, up, down, total):
    queue = deque([start])
    visited[start] = 1
    while queue:
        current = queue.popleft()

        if current == end:
            return visited[current] - 1
        
        moves = [current+up, current-down]

        for move in moves:
            if 0 < move <= total and visited[move] == 0:
                visited[move] = visited[current] + 1
                queue.append(move)

    return "use the stairs"

print(bfs(S,G,U,D,F))

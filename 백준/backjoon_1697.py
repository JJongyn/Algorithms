'''
https://www.acmicpc.net/problem/1697

'''

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0 for _ in range(1000001)]

def search(start, end):
    queue = deque([start])
    while queue:
        current = queue.popleft()
        if current == end:
            return visited[current]
        
        moves = [current+1, current-1, current*2]

        for next in moves:
            if next < 0 or next >= 100001:
                continue
            if visited[next] == 0:
                visited[next] = visited[current] + 1
                queue.append(next)

print(search(N, K))

        

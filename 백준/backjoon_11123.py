import sys

input = sys.stdin.readline
sys.setrecursionlimit(3000000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search(x, y):
    graph[x][y] = '.'

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < H and 0 <= ny < W and graph[nx][ny] == '#':
            search(nx, ny)

T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(H)]  
    result = 0
    for i in range(H):
        for j in range(W):
             if graph[i][j] == '#':
                search(i, j)
                result += 1
    print(result)        

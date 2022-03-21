from collections import deque

def DFS(x, y, n):

    if len(str(n)) == 6:
        if n not in num_list:
            num_list.append(n)
        return

    for i in range(4):  # 이동가능한 방향은 최대 4
        next_x = x + dx[i]
        next_y = y + dy[i]

        # 벽을 넘어갈 경우 x
        if next_x < 0 or next_y < 0 or next_x >= 5 or next_y >= 5: # (0,0)~(4,4)
            continue

        # 이전 재귀적으로 호출
        else:
            DFS(next_x, next_y, n+graph[next_x][next_y])


graph = []
for i in range(5):
    graph.append(list(map(str, input().split())))

# 이동방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

num_list = []
for i in range(5):
    for j in range(5):
        DFS(i,j,graph[i][j])

print(len(num_list))
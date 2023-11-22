dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    global cnt
    
    array[x][y] = 0
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < N:
            if array[nx][ny] == 1:
                dfs(nx, ny)
                
N = int(input())

# 맵 구성
array = []
for _ in range(N):
    array.append(list(map(int, input())))
    
# 탐색
result = []
for i in range(N):
    for j in range(N):
        if array[i][j] == 1: # 집이 있다면    
            cnt = 0
            dfs(i, j)
            result.append(cnt) # 최소 1개

result.sort()
print(len(result))
for i in result:
    print(i)

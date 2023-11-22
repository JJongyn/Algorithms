import sys
sys.setrecursionlimit(10000)


def dfs(x, y):
    dx = [1, -1, 0 , 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i] # 좌, 우
        ny = y + dy[i] # 상, 하
        
        if 0<=nx<N and 0<=ny<M: # in array
            if array[nx][ny] == 1: # 배추가 있을 때 
                array[nx][ny] = 0 # 상하좌우는 다 벌레가 없어도 된다
                dfs(nx, ny)

    
n = int(input())
for i in range(n):
    M, N, K = map(int, input().split())
    array = [[0]*M for _ in range(N)]
    
    # 배추 위치 생성
    for _ in range(K):
        X, Y = map(int, input().split())
        array[Y][X] = 1
    
    # 모든 위치 확인    
    result = 0
    for i in range(N): 
        for j in range(M): 
            if array[i][j] > 0:
                dfs(i,j)
                result += 1
    print(result)
            
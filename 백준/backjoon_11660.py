import sys
N, M = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# array에 반대로 넣어야 함
prefix = [[0] * (N+1) for _ in range(N+1)]       

for i in range(1, N+1):
    for j in range(1, N+1):
        prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1] + array[i-1][j-1] # 마지막은 겹치는 부분 

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1])
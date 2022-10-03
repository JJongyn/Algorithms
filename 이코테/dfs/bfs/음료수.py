'''
[이코테] 음료수 얼려 먹기

구멍이 뚫려 있는 부분은 0, 칸막이는 1
생성되는 총 아이스크림의 수

'''

N, M = map(int, input().split())
array = []
for i in range(N):
    array.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= N or y<= -1 or y >= M:       # 맵을 벗어나는 경우에는 False
        return False
    if array[x][y] == 0:                            # 현재 0인 곳을 시작으로
        array[x][y] = 1                             # 방문처리를 해준다.
        dfs(x-1, y)                     
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True                                 # 기준점을 기준으로 상, 하, 좌, 우를 재귀적으로 탐색함 -> 끝까지 가면 True -> cnt ++
    return False                                    # 1인 곳은 False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)
        
        
        


N, M = map(int, input().split())
x, y, d = map(int, input().split())

# 방문
visited = [[0]*M for _ in range(N)]

# 맵
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

dx, dy = 0, 0
movement = [(-1, 0), (0, 1), (1, 0), (0, -1)]                     # 북, 동, 남, 서

# 회전
def turn():
    global d
    d -= 1 
    if d == -1:d = 3

turn_cnt = 0
result = 0
while True: 
    turn()                                                        # 왼쪽으로 회전
    dx = x + movement[d][0]                                       # 이동할 방향
    dy = y + movement[d][1]                 
    
    if data[dx][dy] == 0 and visited[dx][dy] == 0:                # 이동이 가능하면
        x, y = dx, dy
        visited[dx][dy] = 1                                       # 방문했음을 표시
        result += 1
        turn_cnt = 0
        continue
    else:                                                         # 이동이 불가능하면
        turn_cnt += 1                                             # 상, 하, 좌, 우 확인
    
    if turn_cnt == 4:
        dx = x - movement[d][0]                                   # 반대 방향으로 이동
        dy = y - movement[d][1]             
        
        if data[dx][dy] == 1:
            break
        else:
            x, y = dx, dy
        turn_cnt = 0

print(result)

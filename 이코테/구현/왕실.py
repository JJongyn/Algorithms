n = input()

row = ord(n[0]) - 96
col = int(n[1])

x, y = col, row                                 # 현재 위치
dx, dy = 0, 0                                   # 이동 거리 초기화
result = 0                                      

                                                
movement = [(2, 1), (2, -1), (-2, 1), (-2, -1), # 이동가능한 모든 경우
            (1, 2), (1, -2), (-1, 2), (-1, -2)] # [y, x] = [위-아래, 왼쪽-오른쪽]

    
for move in movement:                           # 이동가능한 경우에 대해 모두 탐색 
    dx = x + move[1]                            # 이동했을 경우 x 위치
    dy = y + move[0]                            # 이동했을 경우 y 위치
    
    if dx < 1 or dx > 8 or dy < 1 or dy > 8:    # 지도를 벗어나는 경우
        continue
    else:
        result += 1

print(result)
        
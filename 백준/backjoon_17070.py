import sys
from collections import deque

'''
(1,1) (1,2) => (x1,y1) - (x2, y2) 한 묶음

<조건> x1 < x2, y1 < y2
    x1 == x2: 가로
    y1 == y2: 세로
    x1 + 1 == x2 and y1 + 1 == y2: 대각선

89% 시간 초과 
'''

input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
result = 0

def get_state(x1, y1, x2, y2):
    if x1 == x2:
        return [0, 1], [1, 1]
    elif y1 == y2:
        return [1, 1], [0, 1]
    elif x1 + 1 == x2 and y1 + 1 == y2:
        return [0, 1, 1], [1, 0, 1]

def check_arrival(x, y):
    return True if (x==N-1 and y==N-1) else False

def search(x1,y1,x2,y2):
    global result

    stack = deque()
    stack.append([x1, y1, x2, y2])

    ######   이거는 질문 게시판 참고 했음.....  ######
    if graph[N-1][N-1] == 1:
        result = 0
        return 
    ############################################

    while stack:
        cx1, cy1, cx2, cy2 = stack.pop()
        dx, dy = get_state(cx1, cy1, cx2, cy2)
        for i in range(len(dx)):
            nx1, ny1 = cx2, cy2
            nx2, ny2 = cx2 + dx[i], cy2 + dy[i]

            if nx2 < 0 or nx2 >= N or ny2 < 0 or ny2 >= N:
                continue
            
            if graph[nx2][ny2] == 0:
                if (dx[i] + dy[i]) == 2: # 대각선 이동 시 왼쪽과 위쪽을 확인
                    if graph[nx2][ny2-1] != 0 or graph[nx2-1][ny2] != 0:
                        continue
                # 이동 가능한 경로이면 도착 지점 확안하기
                if check_arrival(nx2, ny2):
                    result += 1
                else:
                    stack.append([nx1, ny1, nx2, ny2])
            
                
search(0, 0, 0, 1)
print(result)
            
                
            
    






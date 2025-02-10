import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    start_x, start_y = map(int, input().split())
    conv_list = [list(map(int, input().split())) for _ in range(n)]
    conv_visited = [False for _ in range(n)]
    finish_x, finish_y = map(int, input().split())

    def cal_dist(x1,y1,x2,y2):
        # print('a',abs(x1-x2) + abs(y1-y2))
        return abs(x1-x2) + abs(y1-y2)
    
    # 50 * 20 = 1000, 1000보다 거리 작으면 편의점 들려야 함
    def search(x1, y1):
        q = deque()
        q.append([x1,y1])
        while q:
            x, y = q.popleft()

            if cal_dist(x,y,finish_x,finish_y) <= 1000: return 'happy' # 만약에 현재 위치 ~ 페스티벌 갈 수 있으면 리턴

            for i in range(n): # 편의점
                if conv_visited[i] == False:
                    c_x, c_y = conv_list[i]

                    if cal_dist(x,y,c_x,c_y) > 1000: # 현재 위치에서 편의점 못 가면 X
                        continue

                    q.append([c_x, c_y])
                    conv_visited[i] = True
        return 'sad'

    print(search(start_x, start_y))








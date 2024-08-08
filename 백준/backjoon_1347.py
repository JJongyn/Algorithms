'''
https://www.acmicpc.net/problem/1347
'''

import sys

input = sys.stdin.readline

N = int(input())
moves = input().rstrip()

dx, dy = [0, -1, 0, 1], [1, 0, -1, 0] # 남 서 북 동
min_x, max_x, min_y, max_y = 0, 0, 0, 0
pos = [[0,0]] # x, y
direction = 0 # 0, 1, 2, 3 / 남 서 북 동

for move in moves:
    if move == 'R':
        direction = (direction + 1) % 4
    elif move == 'L':
        direction = (direction - 1) % 4
    else:
        current_x, current_y = pos[-1][0], pos[-1][1]
        move_x, move_y = current_x + dx[direction], current_y + dy[direction]
        min_x, min_y = min(move_x, min_x), min(move_y, min_y)
        max_x, max_y = max(move_x, max_x), max(move_y, max_y)
        pos.append([move_x, move_y])

w, h =  abs(max_x - min_x) + 1, abs(max_y - min_y) + 1
maps = [['#'] * w for _ in range(h)]
for p in pos:
    x, y = p[0], p[1]
    maps[y-min_y][x-min_x] = '.'

for m in maps:
    print(''.join(m))


    
    








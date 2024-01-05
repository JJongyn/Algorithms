'''
https://school.programmers.co.kr/learn/courses/30/lessons/154540
'''
from collections import deque

def solution(maps):
    
    def bfs(x, y, maps, visited):
        mX = [0,1,-1,0]
        mY = [1,0,0,-1]
        
        q = deque()
        q.append((x,y))
        
        item = int(maps[x][y])
        visited[x][y] = 1
        
        while q:
            x_, y_ = q.popleft()
            
            for i in range(4):
                nx = x_ + mX[i]
                ny = y_ + mY[i]
                
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                    if maps[nx][ny] != 'X' and visited[nx][ny] == 0:
                        q.append((nx, ny))
                        visited[nx][ny] = 1
                        item += int(maps[nx][ny])
                    
        return item
    
    
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    result = []
    for x in range(len(maps)):
        for y in range(len(maps[0])):
            if maps[x][y] != 'X' and visited[x][y] == 0:
                result.append(bfs(x, y, maps, visited))
    if result:
        return sorted(result)
    else:
        return [-1]
    
    return visited
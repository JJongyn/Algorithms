'''
https://school.programmers.co.kr/learn/courses/30/lessons/120866
'''

import copy

def solution(board):
    visited = copy.deepcopy(board)
    current = sum(sum(board, []))
    cnt = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx = i + dx
                        ny = j + dy
                        if nx >= 0 and ny >= 0 and nx < len(board) and ny < len(board):
                            if visited[nx][ny] != 1:
                                cnt += 1
                                visited[nx][ny] = 1
    answer = cnt+current
    
    return len(board)**2 - answer
import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(N)]

cases = [[(0,1), (0,2), (0,3)], [(1,0), (2,0), (3,0)], # 1x4 형태 
        [(0,1), (1,0), (1,1)], # 2x2형태
        [(1,0),(1,1),(2,1)], [(0,-1), (1,-1), (1,-2)], # ㄹ자 (회전)
        [(1,0), (1,-1), (2,-1)],[(0,1), (1,1), (1,2)], # ㄹ자 (대칭)
        [(1,0), (2,0), (2,1)], [(0,1), (0,2), (1,0)], # ㄴ자 (회전)
        [(0,1),(1,1), (2,1)], [(0,1), (0,2), (-1,2)],
        [(1,0),(2,0),(2,-1)],[(0,1),(0,2),(1,2)], # ㄴ자 (대칭)
        [(1,0),(2,0),(0,1)], [(1,0),(1,1),(1,2)],
        [(1,0),(1,1),(1,-1)], [(1,0),(1,1),(2,0)], # ㅗ자(회전)
        [(0,-1),(1,0),(0,1)],[(0,1),(-1,1),(1,1)]]

def cal_case(i, j, case):
    ans = graph[i][j]
    for a, b in case:
        current_i, current_j = i+a, j+b
        if 0 <= current_i < N and 0 <= current_j < M:
            ans += graph[current_i][current_j]
    return ans

result = 0
for i in range(N):
    for j in range(M):
        for c in cases:
            result = max(cal_case(i, j, c), result)

print(result)
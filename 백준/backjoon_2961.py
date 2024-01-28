'''
240129
실버2. https://www.acmicpc.net/problem/2961

전체 경우 중 최소를 찾아야함.
반복되는 부분이 있음(이전 재료를 다음에도 사용하는 경우)
따라서 backtraking으로,

[입력]
2
3 8
5 8

[출력]
1
'''

# N = int(input())
# data = [list(map(int,input().split())) for _ in range(N)]
# visited = [False] * N

# results = []

# def back_traking(start, a, b):    
#     if start >= 1: # 재료를 1개 이상 사용
#         results.append(abs(a-b))

#     for i in range(start, N):
#         if not visited[i]:            
#             c, d = data[i]
#             visited[i] = True
#             back_traking(start+1, a*c, d+b)
#             visited[i] = False

# back_traking(0, 1, 0)
# print(min(results))

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
ans = 1e9

def dfs(depth, cnt, a, b):
    if cnt != 0:
        ans = min(abs(a-b), ans)
    
    if depth == N:
        return
    
    dfs(depth+1, cnt+1, data[depth][0] * a, data[depth][1]+b)
    dfs((depth+1, cnt, a, b))
    
    
    
dfs(0, 0, 1, 0) # 깊이, 개수, 쓴 맛, 신 맛
'''

실버2. https://www.acmicpc.net/problem/1182

'''

N, S = map(int, input().split())
data = list(map(int, input().split()))

lst = []
cnt = 0

def dfs(start):
    global cnt
    if len(lst) > 0 and sum(lst) == S:
        cnt += 1
        
    for i in range(start, N):
        lst.append(data[i])
        dfs(i+1)
        lst.pop()
        
dfs(0)
print(cnt)
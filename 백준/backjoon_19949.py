'''
실버2. https://www.acmicpc.net/problem/19949

3개의 연속된 문제의 답은 같지 않게.
점수가 5점 이상일 경우
'''


solution = list(map(int, input().split()))
visited = [0, 0, 0, 0, 0, 0]
ans = 0
def dfs(lst):
    global ans
    if len(lst) == len(solution):
        new = [i-j for i, j in zip(lst, solution)]
        if new.count(0) >= 5:
            ans += 1
        return
    
    for i in range(1, 6):
        if len(lst) < 2:
            dfs(lst + [i])
            
        elif not (lst[-1] == lst[-2] == i):
            dfs(lst + [i])
dfs([])
print(ans)
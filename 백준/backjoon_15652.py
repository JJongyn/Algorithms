'''
https://www.acmicpc.net/problem/15652
'''



N, M = map(int, input().split())

# def dfs(lst):
#     if len(lst) == M:
#         results.append(lst)
#         return
    
#     for i in range(1, N+1):
#         if lst == []:
#             dfs(lst + [i])
#         elif lst and lst[-1] <= i:
#             dfs(lst + [i])

# results = []
# dfs([])
# for result in results:
#     print(*result)

N, M = map(int, input().split())
def dfs(start):
    if len(lst) == M:
        print(*lst)
        return
    
    
    for i in range(start, N+1):
        lst.append(i)
        dfs(i)
        lst.pop()
lst = []        
dfs(1)

'''
실버1. https://www.acmicpc.net/problem/1342

값을 추가할 떄 마다 이전 값이 지금이랑 같은지 확인하고 재귀로 동작?
'''


# data = input()
# visited = [False] * len(data)
# ans = 0
# results = []
# def dfs(lst):
#     global ans
#     global results
#     if len(lst) == len(data):
#         if ''.join(lst) not in results: # 여기서 for문을 또 탐색해야함 .
#             ans += 1
#             results.append(''.join(lst))
#         return

#     for i in range(len(data)):
#         if len(lst) == 0 or (len(lst) >= 1 and lst[-1] != data[i]): #or (lst[-1] != data[i] and lst[-2] != data[i]):
#             if not visited[i]:
                
#                 lst.append(data[i])
#                 visited[i] = True
#                 dfs(lst)
#                 lst.pop()
#                 visited[i] = False

# dfs([])
# print(ans)
from collections import Counter

data = input()
counter = Counter(data)

def dfs(depth, pre):
    ans = 0
    if depth == len(data):
        return 1
    
    for i in counter.keys():
        if i == pre or counter[i] == 0:
            continue
        
        counter[i] -= 1
        ans += dfs(depth + 1, i)
        counter[i] += 1
    return ans
print(dfs(0, ''))
    
    

    

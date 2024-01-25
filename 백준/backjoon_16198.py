
N = int(input())
lst = list(map(int, input().split()))


def dfs(energy):
    if len(lst) == 2:
        results.append(energy)
        return 
    
    for i in range(1, len(lst) - 1):
        target = lst[i-1] * lst[i+1]
        k = lst[i]
        del lst[i]
        dfs(target + energy)
        lst.insert(i, k)
    
    
results = []
dfs(0)
print(results)
print(max(results))
# def dfs(tmp):
#     global ans
#     if len(a) == 2:
#         print(tmp)
#         if ans < tmp:
#             ans = tmp
#         return
#     else:
#         for i in range(1, len(a) - 1):
#             k = a[i]
#             del a[i]
#             dfs(tmp + a[i - 1] * a[i])
#             a.insert(i, k)


# N, a = int(input()), list(map(int, input().split()))
# ans = 0
# dfs(0)
# print(ans)
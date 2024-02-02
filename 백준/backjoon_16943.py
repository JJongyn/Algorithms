'''
실버1. 

https://www.acmicpc.net/problem/16943

1234 3456
-> 3421
'''


a, b = input().split()

visited = [False] * len(a)
best = -1
def dfs(number):
    global best
    if len(number) == len(a):
        if int(''.join(number)) > best and  number[0] != '0' and int(''.join(number)) < int(b):
            best = int(''.join(number))
        return  

    for i in range(len(a)):
        if not visited[i]:
            visited[i] = True
            number.append(a[i])
            dfs(number)
            number.pop()
            visited[i] = False

dfs([])    
print(best)

from itertools import permutations

a, b = input().split()
b = int(b)
best = -1

arr = [''.join(i) for i in permutations(a)]


for item in arr:
    if item[0] == '0':
        continue
    if int(item) > best and int(item) < b:
        best = int(item)
print(best)
        
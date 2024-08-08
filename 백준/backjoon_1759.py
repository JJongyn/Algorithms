'''
https://www.acmicpc.net/problem/1759
'''


import sys

input = sys.stdin.readline

L, C = map(int, input().split())
data = sorted(list(input().rstrip().split()))
condition = ['a', 'e', 'i', 'o', 'u']

# 조건 1 : 모음 1개, 자음 2개
# 조건 2 : 오름 차순 (==) sorted

lst = []
results = []
def search(st):
    
    if len(lst) == L: 
        a, b = 0, 0 
        for i in lst:
            if i in condition:
                a += 1
            else:
                b += 1
        
        if a >= 1 and b >= 2:
            results.append(''.join(lst))
        
    for i in range(st, C):
        if data[i] not in lst:
            lst.append(data[i])
        search(i+1)
        lst.pop()

## main
search(0)
print(*sorted(results), sep='\n')


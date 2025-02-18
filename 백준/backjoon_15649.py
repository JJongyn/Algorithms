import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

def search(num):
    
    if len(num) == M:
        print(*num)
        return
    
    for i in range(1, N+1):
        if i not in num:
            num.append(i)
            search(num)
            num.pop()

search([])
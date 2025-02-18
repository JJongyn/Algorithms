import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

result = []
def search(start):
    if len(result) == M:
        print(*result)
        return
    
    for i in range(start, N+1):
        if i not in result:
            result.append(i)
            search(i+1)
            result.pop()

search(1)

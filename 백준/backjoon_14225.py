import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))

result = [0] + [-1 for _ in range(2000000)]

visited = [False for _ in range(N+1)]

data = []
def search(start):
    result[sum(data)] = sum(data)
    
    for i in range(start, N):
        if not visited[i]:
            data.append(S[i])
            visited[i] = True
            search(i)
            visited[i] = False
            data.pop()
    return

search(0)
print(result.index(-1))


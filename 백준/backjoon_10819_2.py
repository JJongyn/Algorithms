import sys

input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

best = -float('inf')
temp = []
visited = [False] * N
def search(depth):
    global best
    if depth == N:
        num = sum(abs(temp[i] - temp[i+1]) for i in range(N-1))
        best = max(best, num)
        return
    
    for i in range(N):
        if not visited[i]:
            temp.append(data[i])
            visited[i] = True
            search(depth+1)
            temp.pop()
            visited[i] = False

search(0)
print(best)
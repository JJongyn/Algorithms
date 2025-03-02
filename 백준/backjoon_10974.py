import sys

input = sys.stdin.readline
N = int(input())

data = []
def search(i):
    if len(data) == N:
        print(*data)
        return
    
    for j in range(1, N+1):
        if j not in data:
            data.append(j)
            search()
            data.pop()

search(1)
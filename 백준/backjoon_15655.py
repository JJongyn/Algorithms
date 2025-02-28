import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))
data = sorted(list(map(int, input().split())))

dump = []
def search(start):
    if len(dump) == M:
        print(*dump)
        return
    for i in range(start, N):
        dump.append(data[i])
        search(i+1)
        dump.pop()
        
search(0)
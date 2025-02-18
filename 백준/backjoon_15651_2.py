import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

result = []
def search(start):
    if len(result) == M:
        print(*result)
        return

    for i in range(1, N+1):
        result.append(i)
        search(i)
        result.pop()

search(1)

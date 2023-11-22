import sys

N, M = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

sum = 0
prefix = [0]
for i in data:
    sum += i
    prefix.append(sum)
    
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(prefix[j] - prefix[i - 1])
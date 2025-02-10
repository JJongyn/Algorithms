import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int,input().split()))

for i in range(m):
    data.sort()
    s = data[0] + data[1]
    data[0], data[1] = s, s
print(sum(data))



import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    if data[i] < data[i-1]:
        pivot = i-1
        for j in range(n-1, 0, -1):
            if data[pivot] > data[j]:
                data[pivot], data[j] = data[j], data[pivot]
                data = data[:i] + sorted(data[i:], reverse=True)
                print(*data)
                exit()
print(-1)
    



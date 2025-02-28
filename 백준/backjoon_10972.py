import sys

input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

swap = False
for i in range(N-1, 0, -1):
    if data[i] > data[i-1]: # i - 1 = pivot
        for j in range(N-1, 0, -1):
            if data[j] > data[i-1]:
                data[i-1], data[j]= data[j], data[i-1]
                data = data[:i] + sorted(data[i:])
                print(*data)
                exit()
print(-1)
                
        
        
    
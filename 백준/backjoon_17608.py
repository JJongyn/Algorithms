import sys

n = int(sys.stdin.readline())
data=[]
for i in range(n):
    data.append(int(sys.stdin.readline()))

cnt = 1
std = data[-1]
for i in range(n-1, -1, -1):
    # 오른쪽이 왼쪽보다 커야함
    if data[i] > std:
       cnt+=1
       std = data[i]
print(cnt)
import sys

n = int(sys.stdin.readline())

data = []
for i in range(n):
    data.append(sys.stdin.readline().rstrip())

data = list(set(data))
data.sort() # 사전 순으로 정렬
data.sort(key=lambda x:len(x)) # 길이를 기준으로 정렬

for i in range(len(data)):
    print(data[i])
import sys

data = []
N, K = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]



# ice 를 다 잡는걸 생각 못햇다!
ice = [0]*1000001 # 최대 얼음의 수
for i in range(N):
    ice[data[i][1]] = data[i][0] # 얼음의 위치에 무게 넣기

# 여기는 생각했지만..
next = 2*K + 1  
window = sum(ice[:next])
result = window

for i in range(next, 1000001):
    window = window + (ice[i] - ice[i-next])
    result = max(result, window) # 이 부분 기억하기!!!!
print(result)
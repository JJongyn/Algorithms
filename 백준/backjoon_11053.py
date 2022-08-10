import sys


n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

dp = [1] * 1001


for i in range(1, n):  # 현재 dp에 담긴 값이 가장 큰 인덱스를 반환 받아서 그 크기보다 커야함
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
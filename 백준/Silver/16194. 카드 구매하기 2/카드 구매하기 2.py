N = int(input())
dp = [0]+list(map(int,input().split()))

for i in range(N+1):
    for j in range(1,i+1):
        dp[i] = min(dp[i],dp[i-j]+dp[j])
print(dp[N])
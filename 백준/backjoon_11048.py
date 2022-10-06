n, m = map(int, input().split())

# 미로 만들기
array = []
for i in range(n): array.append(list(map(int, input().split())))

# memoization 공간 
d = []
for i in range(n+1):d.append([0] * (m+1))

# 미로 돌면서 상, 하, 대각선 중 최대 사탕을 얻을 수 있는 곳으로 이동
for i in range(1, n+1):
    for j in range(1, m+1):
        d[i][j] = array[i-1][j-1] + max(d[i-1][j], d[i][j-1], d[i-1][j-1])
        
print(d[n][m])
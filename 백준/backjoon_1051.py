'''
실버2 
https://www.acmicpc.net/problem/1051
[입력]
3 5
42101
22100
22101

'''

N, M = map(int, input().split())
maps = []

for _ in range(N):
    maps.append(list(map(int, input())))

best_area = 1
for i in range(N):
    for j in range(M-1):
        for k in range(j+1, M):
            if maps[i][j] == maps[i][k]:
                if i + k - j < N and maps[i+k-j][j] == maps[i][j] and maps[i+k-j][k] == maps[i][j]:
                    area = (k - j + 1) ** 2
                    if area > best_area:
                        best_area = area
                
print(best_area)
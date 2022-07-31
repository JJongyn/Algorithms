import sys

# N = int(sys.stdin.readline())
# data = []
data = [list(sys.stdin.readline().strip()) for _ in range(8)]

cnt = 0
for i in range(8): # 행
    for j in range(8): # 열
        if i % 2 == 0 and j % 2 == 0:
            if data[i][j] == 'F': cnt += 1
        elif i % 2 != 0 and j % 2 != 0:
            if data[i][j] == 'F': cnt += 1

print(cnt)



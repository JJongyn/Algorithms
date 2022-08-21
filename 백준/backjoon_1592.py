import sys

N, M, L = map(int ,sys.stdin.readline().rstrip().split())
data = [0] * N

i = 0
cnt = 0
while(True):
    data[i] += 1
    if data[i] == M:
        print(cnt)
        break

    if data[i] % 2 == 0:
        i = (i + N - L) % N
    else:
        i = (i + L ) % N
    cnt += 1
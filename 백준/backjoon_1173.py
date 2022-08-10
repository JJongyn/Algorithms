import sys
# N, m, M, T, R
N,m,M,T,R = map(int, sys.stdin.readline().split())

cnt = 0;time=0
current = m

while(cnt < N):
    if m + T > M:
        break
    if current + T <= M:
        cnt+=1
        time+=1
        current += T
    else:
        current = max(current-R, m)
        time +=1

if cnt == N:
    print(time)
else:print(-1)
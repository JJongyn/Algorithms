import sys

N, K = sys.stdin.readline().split()
data = list(map(int, sys.stdin.readline().split()))

N = int(N)

end = 0
cnt_lion = 0 # 라이언 인형 수
cnt = 0 # 원소의 수 
cnt_min = sys.maxsize # 정답
for start in range(N):

    while(end < N and cnt_lion < int(K)):
        cnt += 1
        if(data[end] == 1):
            cnt_lion += 1
        end += 1

    if cnt_lion == int(K) and cnt_min > cnt:
        cnt_min = cnt

    if data[start] == 1:
        cnt_lion -= 1
    cnt -= 1    


if cnt_min != sys.maxsize:
    print(cnt_min)
else:print(-1)
 
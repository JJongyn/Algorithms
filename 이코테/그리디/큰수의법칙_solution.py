
'''
주어진 수들을 M번 더하여 가장 큰 수를 만들어야 한다.
해당하는 수가 연속해서 K번 초과하여 더해질 수 없다.

--> M이 커지면 for or while에서 시간초과가 날 것임. 그러니 수학식으로 풀면 아래와 같음.
'''
N, M, K = map(int,input().split())
data = list(map(int, input().split()))

data.sort()
second_num = data[-2]
first_num = data[-1]

result = 0
# 첫 번째 수 cnt
cnt = M // (K+1) * K
cnt = cnt + M % (K+1)

result += first_num * cnt
result += second_num * (M - cnt )

print(result)   
        


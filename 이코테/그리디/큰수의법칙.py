
'''
주어진 수들을 M번 더하여 가장 큰 수를 만들어야 한다.
해당하는 수가 연속해서 K번 초과하여 더해질 수 없다

'''
N, M, K = map(int,input().split())
data = list(map(int, input().split()))

data.sort()
second_num = data[-2]
first_num = data[-1]

result = 0
cnt = 0
flag = True
for i in range(M):
    
    if cnt == K:
        flag = False
        
    if flag:
        result += first_num
        cnt += 1
    else:
        result += second_num
        flag = True
        cnt = 0

print(result)   
        


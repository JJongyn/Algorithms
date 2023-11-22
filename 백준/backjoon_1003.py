'''
# 시간초과
def fibo(n):
    global cnt_0
    global cnt_1
    if n == 0:
        cnt_0 += 1
        return cnt_0, cnt_1
    elif n == 1:
        cnt_1 += 1
        return cnt_0, cnt_1
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input())
for i in range(n):
    num = int(input())
    cnt_0, cnt_1 = 0, 0
    fibo(num)
    print(cnt_0, cnt_1)
    
'''

n = int(input())

d_0 = [1, 0]
d_1 = [0, 1]

for i in range(2, 41):
    d_0.append(d_0[i-1] + d_0[i-2]) # zero
    d_1.append(d_1[i-1] + d_1[i-2]) # one
    
for j in range(n):
    num = int(input())
    print(d_0[num], d_1[num])
    
#fibo = int(input())
    

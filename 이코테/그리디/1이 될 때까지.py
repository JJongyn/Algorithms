import time

start_time = time.time()
n, k = map(int, input().split())

result = 0
while(n>1):
    if n % k == 0:
        result += 1
        n = n / k
    else:
        n -= 1
        result += 1
end_time = time.time()
print("소요 시간:{:0.2f}s".format(end_time-start_time))
print(result)

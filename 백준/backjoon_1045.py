import sys

data = list(map(int, sys.stdin.readline().split()))
#print(data)

min_data = min(data)

while(True):
    cnt = 0
    for i in data:
        if min_data % i == 0:
            cnt += 1
    
    if cnt >= 3:
        print(min_data)
        break

    min_data+=1
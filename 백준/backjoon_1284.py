import sys

while(True):
    data = []
    n = input()
    if n == '0':break
    
    for i in n:
        data.append(i)
    
    sum = 1
    for i in data:
        sum += 1
        if i == '1':sum+=2
        elif i == '0':sum+=4
        else:sum+=3
    print(sum)
    
import sys

a, b = map(int, sys.stdin.readline().split())

sum = 0
cnt = 1
for i in range(1, b+1):
    for j in range(i):

        if cnt >=a and cnt <=b:
            sum += i
        if cnt > b : break
        cnt +=1

print(sum)
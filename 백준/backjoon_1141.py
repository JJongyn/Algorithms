import sys

input = sys.stdin.readline

data = []
for _ in range(int(input())):
    data.append(input().rstrip())

'''
[hello, hi, h, run, rerun, running]

sort: [h, hi, run, rerun, hello, running]

h -> [h, run, rerun, running]
hi -> [hi, run, rerun, hello, running]
run -> [run, rerun, hello]
rerun -> [rerun, hello, running]
hello -> [hello, running]
running -> [running]

'''


data.sort(key=len)
data = list(set(data))

cnt = len(data)
for i in range(len(data)):
    criterion = data[i]
    for j in range(len(data)):
        if i != j and (data[j].startswith(criterion)):
            cnt -= 1
            break

print(cnt)
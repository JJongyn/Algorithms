import sys

input = sys.stdin.readline

first = input().rstrip()
second = input().rstrip()


if len(first) > len(second):
    short, long = second, first
else:
    short, long = first, second

total_len = len(short) + len(long)
long_all = long.ljust(total_len, '0').rjust(total_len+len(short), '0')


# 짧은 기어 이동하면서 비교
result = total_len
for i in range(1, len(long_all)-len(short)):
    long_temp = long_all[i:i+len(short)]
    
    flag = True
    for j in range(len(short)):
        if long_temp[j] == '2' and short[j] == '2':
            flag=False
            continue
    if flag:
        # total_len - 겹치는 부분 
        shared_part = long_temp.strip('0')
        result = min(result, total_len - len(shared_part))
    
print(result)

            
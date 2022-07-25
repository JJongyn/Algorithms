import sys

data_list = []
n = int(sys.stdin.readline())
for i in range(n):
    data = int(sys.stdin.readline())
    if data == 0 and data_list:
        data_list.pop()
    else:
        data_list.append(data)
    #print(data_list)
print(sum(data_list))
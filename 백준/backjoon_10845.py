import sys

que = []
n = int(sys.stdin.readline())
for i in range(n):
    data = sys.stdin.readline().split()
    # push
    if(data[0] == "push"):que.append(data[1])
    elif(data[0] == "pop"):
        if que: 
            dump = que.pop(0)
            print(dump)
        else:print(-1)
    elif(data[0] == "size"):print(len(que))
    elif(data[0] == "empty"):
        if que:print(0)
        else:print(1)
    elif(data[0] == "front"):
        if que:print(que[0])
        else:print(-1)
    elif(data[0] == "back"):
        if que:print(que[-1])
        else:print(-1)


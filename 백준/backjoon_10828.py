import sys

stack = []
n = int(sys.stdin.readline())

for i in range(n):
    data = sys.stdin.readline().split()
    # push
    if(data[0] == "push"):stack.append(data[1])
    elif(data[0] == "pop"):
        if stack: 
            dump = stack.pop()
            print(dump)
        else:print(-1)
    elif(data[0] == "size"):print(len(stack))
    elif(data[0] == "empty"):
        if stack:print(0)
        else:print(1)
    elif(data[0] == "top"):
        if stack:print(stack[-1])
        else:print(-1)



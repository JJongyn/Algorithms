import sys

deque = []
n = int(sys.stdin.readline())
for i in range(n):
    data = sys.stdin.readline().split()
    # push
    if(data[0] == "push_front"):deque.insert(0, data[1])
    elif(data[0] == "push_back"):deque.append(data[1])
    elif(data[0] == "pop_front"): # 가장 앞 제거
        if deque: 
            print(deque.pop(0))
        else:print(-1)

    elif(data[0] == "pop_back"): # 가장 뒤 제거
        if deque: 
            print(deque.pop(-1))
        else:print(-1)

    elif(data[0] == "size"):
        print(len(deque))

    elif(data[0] == "empty"):
        if deque:print(0)
        else:print(1)

    elif(data[0] == "front"):
        if deque:print(deque[0])
        else:print(-1)

    elif(data[0] == "back"):
        if deque:print(deque[-1])
        else:print(-1)


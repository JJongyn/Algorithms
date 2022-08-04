import sys


stack = []
data = list(sys.stdin.readline().rstrip())
n = len(data)

result = 0
cnt = 0
i = 0
for i in range(n):
    if data[i] == '(':
        cnt += 1
        stack.append(data[i])

    else:
        if data[i-1] == '(':
            stack.pop()
            result += len(stack)

        else:
            stack.pop() # 짝이 맞으므로 앞에 '(' 지워야함 
            result +=1

    
print(result)
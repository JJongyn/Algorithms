import sys

input = sys.stdin.readline


k = 1
while True:
    data = list(input().rstrip())
    
    # 종료
    if '-' in data:
        break

    # main loop
    stack = []
    for s in data:
        if s == '{':
            stack.append(s)
        else:
            if stack and stack[-1] == '{' and s == '}':
                stack.pop()
            else:
                stack.append(s)
    
    result = 0
    if len(stack) > 0: # {{ : 1번 , }} : 1번, }{ : 2번
        for i in range(0, len(stack), 2):
            if i + 1 < len(stack): 
                start = i
                end = start + 1
                if stack[start] == stack[end]:
                    result += 1
                else:
                    result += 2
    else:
        result = 0

    print(f'{k}. {result}') 

    k += 1

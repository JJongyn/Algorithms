import sys

data = list(sys.stdin.readline().strip()) 
stack = []

tmp = 1 # 곱해지기위한 값
result = 0 # 최종 결과 값으로 밑에서 tmp가 더해지는 형태이겠지

for i in range(len(data)):
    if data[i] == '[': # 열린 괄호면 무조건 곱해주기
        tmp *= 3
        stack.append(data[i]) # 나중에 닫힌 괄호랑 짝을 맞추기 위해 stack에 넣어줘야 함!

    elif data[i] == '(':
        tmp *= 2
        stack.append(data[i])

    elif data[i] == ']': # 닫힌 괄호면 이제 앞에 짝이 있는지 확인해줘야 함
        if not stack or stack[-1] =='(':  # stack이 비어있거나(열린 괄호가 하나도 없다는 뜻), 앞에 짝이 안맞다면 -> 조건에 맞지 않으니깐 0
            result = 0
            break
        if data[i-1] == '[': # 짝이 맞으면
            result += tmp # 여태 곱해준 값을 더해줌
        tmp //= 3
        # 나눠주는 이유는 ([] 맞는 짝을 이미 곱하고 더했으니깐 그 다음 다른 짝이 나올거임 
        # 예를 들어 ([] '[]' 이런식으로 다음 '[]'가 나오면 앞에 (로 인해 2를 곱해서 다시 새로 들어온 []를 계산해야하므로
        stack.pop()
    
    else: 
        if not stack or stack[-1] =='[':  
            result = 0
            break
        if data[i-1] == '(':
            result += tmp 
        tmp //= 2
        stack.pop()

if stack:
    result=0 # 짝이 맞으면 진작에 다 pop으로 삭제 되엇어야 함

print(result)
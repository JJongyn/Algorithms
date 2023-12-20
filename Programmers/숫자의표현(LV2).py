'''
LV2. https://school.programmers.co.kr/learn/courses/30/lessons/12924
'''


def solution(n):
    
    stack = [] 
    answers = [1] # n은 무조건 정답이므로 길이는 1
    for i in range(1, int(n // 2) + 2): # 절반 이상부터는 연속된 값들이 n을 넘어감
        stack.append(i)
        
        while sum(stack) > n: # 합이 더 커지면 가장 작은 수부터 제거
            stack.pop(0)
            
        if sum(stack) == n: # n과 같으면
            answers.append(len(stack)) # 길이를 저장
            stack.pop(0)
            
    return len(list(set(answers))) # 중복되는 길이는 제외


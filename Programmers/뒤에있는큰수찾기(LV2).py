'''
LV2. https://school.programmers.co.kr/learn/courses/30/lessons/154539

'''

def solution(numbers):
    answers = [-1] * len(numbers)
    stack = [1]
    print(stack.pop())
    for idx, target in enumerate(numbers):
        while stack and numbers[stack[-1]] < target:
            answers[stack.pop()] = target
        stack.append(idx)
        
    return answers
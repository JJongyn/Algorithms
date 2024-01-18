'''
LV2. https://school.programmers.co.kr/learn/courses/30/lessons/131704
'''
def solution(order):
    
    stack = []
    idx = 0
    for current_idx in range(1, len(order)+1):
        stack.append(current_idx)
        while stack and order[idx] == stack[-1]:
            stack.pop()
            idx += 1

    return idx
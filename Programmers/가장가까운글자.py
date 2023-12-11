'''
LV.1 https://school.programmers.co.kr/learn/courses/30/lessons/142086
'''

from collections import deque

def solution(s):
    deq = deque()
    answers = []
    for state in s:
        if state in deq:
            idx = deq.index(state)
            answers.append(idx+1)
            deq.appendleft(state)
        else:
            answers.append(-1)
            deq.appendleft(state)
    return answers
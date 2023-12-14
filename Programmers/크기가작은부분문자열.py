'''
LV1. https://school.programmers.co.kr/learn/courses/30/lessons/147355
'''

def solution(t, p):
    return sum([1 for i in range(len(t) - len(p) + 1) if int(t[i:i+len(p)]) <= int(p)])
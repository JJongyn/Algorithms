'''
LV2. https://school.programmers.co.kr/learn/courses/30/lessons/12941
'''
def solution(A,B):
    answers = [ a * b for a, b in zip(sorted(A), sorted(B, reverse=True))]
    return sum(answers)
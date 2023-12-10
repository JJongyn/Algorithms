'''

LV.1 https://school.programmers.co.kr/learn/courses/30/lessons/76501

'''

def solution(absolutes, signs):
    return sum([num if state else -num for num, state in zip(absolutes, signs)])
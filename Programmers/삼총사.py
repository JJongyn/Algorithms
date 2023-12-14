'''
LV.1 https://school.programmers.co.kr/learn/courses/30/lessons/131705
'''

from itertools import combinations

def solution(number):
    answers = 0
    for a, b, c in list(combinations(number, 3)):
        if a+b+c == 0:answers+=1
    return answers
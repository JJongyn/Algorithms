
'''
월간 코드 챌린지 시즌 1. https://school.programmers.co.kr/learn/courses/30/lessons/68644
'''

from itertools import combinations

def solution(numbers):
    data = sorted(list(set([a+b for a, b in list(combinations(numbers,2))])))
    return data
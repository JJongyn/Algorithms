'''
LV2. https://school.programmers.co.kr/learn/courses/30/lessons/131127
'''
from collections import Counter

def solution(want, number, discount):
    my_item = {}
    answer = 0
    for name, num in zip(want, number):
        my_item[name] = num
    for i in range(0, len(discount) - sum(number) + 1):
        if my_item == Counter(discount[i:i+10]):
            answer += 1
    return answer
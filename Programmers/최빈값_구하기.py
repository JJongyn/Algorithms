'''
https://school.programmers.co.kr/learn/courses/30/lessons/120812
'''

from collections import Counter

def solution(array):
        
    new_list = Counter(array).most_common()
    if len(new_list) > 1:
        if new_list[0][1] == new_list[1][1]:
            return -1
        else:
            return new_list[0][0]
    return array[0]
'''
https://school.programmers.co.kr/learn/courses/30/lessons/120923
'''

def solution(num, total):
    if num == 1:
        return [total]
    elif total == 0:
        b = num // 2
        a = list(range(-b, b+1))
        return a
    for current in range(-total, total):
        a = list(range(current, current+num))
        if sum(a) == total:return a


def solution(num, total):
    
    start = (total // num) - (num - 1) // 2
    answer = [i for i in range(start, start+num)]
    
    return answer
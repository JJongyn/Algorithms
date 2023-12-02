'''
https://school.programmers.co.kr/learn/courses/30/lessons/120894
'''

def solution(numbers):
    keys = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    answers = []
    current = ''
    for i in numbers:
        current += i
        if current in keys:
            answers.append(str(keys[str(current)]))
            current = ''
        
    return int("".join(answers))
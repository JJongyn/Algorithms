'''
https://school.programmers.co.kr/learn/courses/30/lessons/148653
'''

def solution(storey):
    num = list(map(int, str(storey)))
    result = 0
    
    while num:
        current = num.pop()
        if (current == 5 and ((num and num[-1] < 5) or not num)) or current < 5:
            result += current
        else:
            result += 10 - current
            if num:
                num[-1] += 1
            else:
                result += 1 # 10, 100, 1000일거니깐 내려주는 값   
            
    return result
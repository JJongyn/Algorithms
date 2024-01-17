'''
LV1. https://school.programmers.co.kr/learn/courses/30/lessons/134240
'''
def solution(food):
    answer = ''
    for i, f in enumerate(food):
        cnt = food[i] // 2 
        answer += (str(i) * cnt)
    
    return answer + '0' + answer[::-1]
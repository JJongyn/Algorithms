'''
https://school.programmers.co.kr/learn/courses/30/lessons/120884
'''

def solution(chicken):
    answer = 0
    while True:
        
        answer += chicken // 10
        chicken = (chicken // 10 + chicken % 10)       

        if chicken < 10:
            break

    return answer
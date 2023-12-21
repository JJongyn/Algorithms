'''
LV2. https://school.programmers.co.kr/learn/courses/30/lessons/42842
'''


def solution(brown, yellow):
    
    total = brown + yellow
    
    for i in range(1, 2000000):
        if total % i == 0: # 가로
            j = total / i # 세로
            if (i-2)*(j-2) == yellow and i >= j:
                return [i, j]

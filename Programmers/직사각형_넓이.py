'''
https://school.programmers.co.kr/learn/courses/30/lessons/120860
'''

def solution(dots):
    answer = 0
    
    x_list = []
    y_list = []
    for x, y in dots:
        x_list.append(x)
        y_list.append(y)
    area = (max(x_list) - min(x_list)) * (max(y_list) - min(y_list)) 
    
    return area
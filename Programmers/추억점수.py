'''
https://school.programmers.co.kr/learn/courses/30/lessons/176963
'''

def solution(name, yearning, photo):
    dic = {}
    for n, y in zip(name, yearning):
        dic[n] = y
    
    answer = []
    for p in photo:
        result = 0
        for name in p:
            if name in dic:
                result += dic[name]
        answer.append(result)
            
            
    return answer
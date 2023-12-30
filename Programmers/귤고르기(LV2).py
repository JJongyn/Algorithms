'''
LV2. https://school.programmers.co.kr/learn/courses/30/lessons/138476

'''

def solution(k, tangerine):
    # k개를 고를 때 크기가 서도 다른 종류의 최솟값
    dic = {}
    for i in list(set(tangerine)): dic[i] = 0
    for i in tangerine:dic[i] += 1
    
    dic = sorted(dic.items(), key=lambda x:-x[1])
    
    result = 0
    for i, (key, item) in enumerate(dic):
        result += item
        
        if result >= k:
            return i+1
        
            
  
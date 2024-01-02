'''
https://school.programmers.co.kr/learn/courses/30/lessons/132265

'''
from collections import Counter

def solution(topping):
    answer = 0
    a = Counter(topping) # 형
    b = set() # 동생
    
    for i in topping:
        a[i] -= 1 # 형에서 하나 제거
        b.add(i)
        if a[i] == 0:
            a.pop(i)
        if len(a) == len(b):
            answer += 1
    return answer
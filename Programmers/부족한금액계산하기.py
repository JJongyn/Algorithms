'''
LV.1 https://school.programmers.co.kr/learn/courses/30/lessons/82612
'''

def solution(price, money, count):
    
    total = sum([i for i in range(price, price*count+1, price)])
    
    if total - money < 0:
        return 0
    else:
        return total - money
    
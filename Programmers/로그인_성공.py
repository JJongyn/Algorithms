'''
https://school.programmers.co.kr/learn/courses/30/lessons/120883
'''

def solution(id_pw, db):
    
    id_flag = 0
    for in_name, in_pw in db:
        if id_pw[0] == in_name and id_pw[1] == in_pw:
            return 'login'
        
        if id_pw[0] == in_name:
            id_flag = 1
            
    if id_flag:
        return 'wrong pw'
    
    return 'fail'
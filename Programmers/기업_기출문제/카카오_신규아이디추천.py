'''
https://school.programmers.co.kr/learn/courses/30/lessons/72410
'''

def solution(new_id):
    data = ''
    for i in new_id.lower(): # 1번
        if i.islower() or i.isdigit() or i == '-' or i == '_' or i == '.': data += i # 2번
    
    # 3번
    while '..' in data:
        data = data.replace('..','.')

    # 4번
    if data[0] == '.':
        if len(data) > 1: 
            data = data[1:]
        else:
            data = '.'
        
    if data[-1] == '.':
        data = data[:-1]
        

    if data == '':
        data = 'a'
    
    # 6번
    if len(data) >= 16:
        data = data[:15]
        if data[-1] == '.': data = data[:-1]

    # 7번
    while len(data) < 3:
        data += data[-1]
    
    return data


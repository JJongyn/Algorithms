'''
[2021 카카오 채용연계형 인턴쉽]
 
LV.1 https://school.programmers.co.kr/learn/courses/30/lessons/81301
'''


def solution(s):
    dic = {'zero':'0',
      'one':'1',
      'two':'2',
      'three':'3',
      'four':'4',
      'five':'5',
      'six':'6',
      'seven':'7',
      'eight':'8',
      'nine':'9'}  
    for key, value in dic.items():
        if key in s:
            s = s.replace(key, value)
    return int(s)
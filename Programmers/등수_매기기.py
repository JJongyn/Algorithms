'''
lv0.
https://school.programmers.co.kr/learn/courses/30/lessons/120882
'''
def solution(score):
    
    s_score = sorted([sum(i) for i in score], reverse=True)
    
    answer = []
    for s in score:
        # index함수는 중복된게 있으면 앞에꺼를 반환
        answer.append(s_score.index(sum(s))+1) 

    return answer
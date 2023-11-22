'''
https://school.programmers.co.kr/learn/courses/30/lessons/42860

고득점 키트 - 그리디 
'''

def solution(name):
    
    result = 0
    
    # 최소 이동 횟수의 초기화는 오른쪽으로 모두 확인하면서 이동할 떄임
    min_move = len(name) - 1
    
    for i, n in enumerate(name):
        result += min(ord(n) - ord('A'), ord('Z')+1 - ord(n))
        
        # 연속된 A가 나오는 곳까지 확인
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        min_move = min([min_move, i * 2 + len(name)-next, i+ (len(name)-next)*2])
        
        
    result += min_move
    
    return result
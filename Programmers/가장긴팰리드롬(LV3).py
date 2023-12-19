'''
LV3. https://school.programmers.co.kr/learn/courses/30/lessons/12904?language=python3
'''

def solution(s):
    answer = 0
    
    def expand(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:

            left -= 1
            right += 1
            
        return s[left+1:right] # if문에서 무조건 -1+1을 해주니깐
    
    if len(s) < 2 or s == s[::-1]:
        return len(s)
    
    result = '' # max인 서브 문자열을 담을 변수
    for i in range(len(s)-1):
        result = max(result, expand(s, i, i+1), expand(s, i, i+2), key=len)
    

    return len(result)
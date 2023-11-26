'''
https://school.programmers.co.kr/learn/courses/30/lessons/120880
'''

# 내 풀이
def solution(numlist, n):
    
    new = []
    for i in range(len(numlist)):
        dif = abs(numlist[i]-n)
        new.append((dif, numlist[i]))
    
    a = sorted(new, key=lambda x: (x[0], -x[1]))
    
    answer = []
    for _, num in a:
        answer.append(num)
        
    return answer

# 같은 방법이지만 더 쉬운 풀이
def solution(numlist, n):
    return sorted(numlist, key=lambda x: (abs(x-n), n-x))
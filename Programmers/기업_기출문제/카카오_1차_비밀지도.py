'''
2018 KAKAO BLIND RECRUITMENT

https://school.programmers.co.kr/learn/courses/30/lessons/17681

'''

def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        data = bin(a|b)[-n:]
        array = ''.join(['#' if i == '1' else ' ' for i in data])
        answer.append(array)
        
    return answer
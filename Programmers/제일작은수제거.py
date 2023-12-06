'''
Lv1. 
https://school.programmers.co.kr/learn/courses/30/lessons/12935
'''

def solution(arr):
    new = arr.pop(arr.index(min(arr)))
    return arr if arr else [-1]
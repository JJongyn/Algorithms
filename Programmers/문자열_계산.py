'''
https://school.programmers.co.kr/learn/courses/30/lessons/120902
'''
def solution(my_string):
    numbers = my_string.split()
    result = int(numbers[0])
    for i, data in enumerate(numbers):
        if data == '+':
            result += int(numbers[i+1])
        elif data == '-':
            result -= int(numbers[i+1])
    return result


def solution(my_string):
    result = sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))
        
    return result
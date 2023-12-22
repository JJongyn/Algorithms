'''
2018 KAKAO BLIND RECRUITMENT 3치

https://school.programmers.co.kr/learn/courses/30/lessons/17686#
'''
def solution(files):
    answers = []
    # TAIL 부분은 상관 x
    for idx, file in enumerate(files):
        file = file.lower() # 대소문자 처리
        answers.append([idx, '', '', ''])
        i = 0
        # HEAD 부분 처리
        while not file[i].isalpha:
            i += 1
        start_s = i
        while not file[i].isdigit():
            answers[-1][1] += file[i]
            i += 1
        # NUMBER 부분 처리
        while i < len(file) and file[i].isdigit():
            answers[-1][2] += file[i]
            i += 1    
        answers[-1][2] = int(answers[-1][2])
        
    answers = sorted(answers, key=lambda x:(x[1], x[2], x[0]))
    results = [files[i[0]] for i in answers]
    return results



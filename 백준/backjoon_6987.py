import sys

input = sys.stdin.readline

con = ['A', 'B', 'C', 'D', 'E', 'F']
dic = {'A':0, 'B': 3, 'C':6, 'D':9, 'E':12, 'F':15} # 나라 + 승패 인덱스 조합


# 승, 패 / 무, 무 / 패, 승
dx = [[-1, 0, 0], [0, -1, 0], [0, 0, -1]]
dy = [[0, 0, -1], [0, -1, 0], [-1, 0, 0]]


def eval(country1, country2, score1, score2):
    c1_idx, c2_idx = dic[country1], dic[country2] 

    c1_win, c1_draw, c1_lose = data[c1_idx], data[c1_idx+1], data[c1_idx+2] # 나라1의 승, 무, 패
    c2_win, c2_draw, c2_lose = data[c2_idx], data[c2_idx+1], data[c2_idx+2] # 나라2의 승, 무, 패

    c1_check = [a + b for a, b in zip([c1_win, c1_draw, c1_lose], score1)]
    c2_check = [a + b for a, b in zip([c2_win, c2_draw, c2_lose], score2)]
    
    if any(x < 0 for x in c1_check) or any(x < 0 for x in c2_check):
        return False
    return True

def update_score(country1, country2, score1, score2):
    c1_idx, c2_idx = dic[country1], dic[country2] 
    for i, score in enumerate(score1):
        data[c1_idx + i] += score

    for i, score in enumerate(score2):
        data[c2_idx + i] += score

def back_score(country1, country2, score1, score2):
    c1_idx, c2_idx = dic[country1], dic[country2] 
    for i, score in enumerate(score1):
        data[c1_idx + i] -= score

    for i, score in enumerate(score2):
        data[c2_idx + i] -= score



stack = []
flag = True
def search(st, flag):
    
    for i in range(st, 6):
        key = con[i] # ex) 'A'
        stack.append(key)
        if len(stack) == 2:
            for j in range(3): 
                score1, score2 = dx[j] ,dy[j]
                if eval(stack[0], stack[1], score1, score2):
                    update_score(stack[0], stack[1], score1, score2)
                    search(j+1, False)
                    back_score(stack[0], stack[1], score1, score2)
                else:
                    stack.pop()
                search(j+1, False)

for i in range(1):
    data = list(map(int, input().split()))
    search(0, True)
    print(data)


# for i in range(3): 
    #     score1, score2 = dx[i] ,dy[i]

    #     if len(stack) == 2:
            
    #         flag = eval(stack[0], stack[1], score1, score2)
    #         if flag == False: # data값이 갱신
    #             return
                
    #     for j in range(st, 6):
    #         key = con[j] # ex) 'A'
    #         stack.append(key)
    #         search(j+1, flag)
    #         if len(stack) > 1 and flag==False:
    #             back_score(stack[0], stack[1], score1, score2)
    #         stack.pop()
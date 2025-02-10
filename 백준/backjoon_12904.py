import sys

input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

'''
B / ABBA
ABBA / B

문자열의 뒤에 A를 제거한다 / B를 제거하고 문자열을 뒤집는다

# 1
ABBA -> ABB (1번)
ABBA -> ABBA (2번)

# 2
ABB -> ABB (1번)
ABB -> AB -> BA (2번)

# 3
BA -> B (1번) 당첨
BA -> AB -> A (2번)

'''
# T = 'AABBBBB'
# print(T[:-1])
# print(T[::-1])

while True:
    if len(T) < len(S):
        print(0)
        break

    if T[-1] == 'A': 
        T = T[:-1]
    else:
        T = T[:-1] # B를 제거하고
        T = T[::-1] # 뒤집기
    
    if T == S:
        print(1)
        break


    
    
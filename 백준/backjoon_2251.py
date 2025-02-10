import sys
from collections import deque

input = sys.stdin.readline

'''
A B C
------
8 9 10

C -> B | 0 9 1
C -> A -> B | 0 8 2

모든 경우의 수 구하기
C -> A
C -> B,
B -> A
B -> C,
A -> B
A -> C

만약, C에서 A로 8을 붓는다면
visited[]

B랑 C가 가지는 물의 양
visited[b의 물][c의 물] = True
visited[<200][<200]
'''

A, B, C = map(int, input().split())
visited = [[False] * 201 for _ in range(201)]
result = set()

def search():
    q = deque()
    q.append((0, 0, C))  # 물의양 
    visited[0][0] = True
    while q:
        a, b, c = q.popleft()  # 현재 물의 양
        if a == 0:  # 종료 조건
            result.add(c)  

        ####### A -> B
        if a + b <= B: # 만약에 a에서 b로 물을 전부 붓는 게 가능하면 
            if not visited[0][a + b]: # b에 a만큼 붓고, 그럼 a는 0
                visited[0][a + b] = True
                q.append((0, a + b, c)) # a는 0, b는 a 더한 거, c는 같음
        else:
            if not visited[a - (B - b)][B]: # b 물컵 다 채워도 남으면, b에는 B만큼, a에는 (B-b)를 뺸 만큼, c는 같음
                visited[a - (B - b)][B] = True
                q.append((a - (B - b), B, c))
        
        ####### A -> C
        if a + c <= C: # 만약에 a에서 c로 물을 전부 붓는 게 가능하면
            if not visited[0][b]: # a는 c한테 줘서 없음, b는 그대로
                visited[0][b] = True
                q.append((0, b, a + c))
        else:
            if not visited[a - (C - c)][b]: # c가 가득차고, a는 (C-c)뻰 만큼, b는 같음
                visited[a - (C - c)][b] = True
                q.append((a - (C - c), b, C))
        
        ####### B -> A
        if a + b <= A:
            if not visited[a + b][0]: # b는 a한테 전부 줌
                visited[a + b][0] = True
                q.append((a + b, 0, c))
        else:
            if not visited[A][b - (A - a)]: # b는 a한테 A가 전부 채워질 수 있는 만큼 줌
                visited[A][b - (A - a)] = True
                q.append((A, b - (A - a), c))
        
        ####### B -> C
        if b + c <= C:
            if not visited[a][0]: # b는 c한테 전부 줌. 그래서 b는 0, a는 그대로
                visited[a][0] = True
                q.append((a, 0, b + c))
        else:
            if not visited[a][b - (C - c)]: # b는 c한테 C가 전부 채워질 수 있는 만큼 줌
                visited[a][b - (C - c)] = True
                q.append((a, b - (C - c), C))
        
        ####### C -> A
        if a + c <= A:
            if not visited[a + c][b]:  # c의 물을 전부 a에 옮김
                visited[a + c][b] = True
                q.append((a + c, b, 0)) 
        else:
            if not visited[A][b]: # a는 A만큼 채워지고
                visited[A][b] = True
                q.append((A, b, c - (A - a))) # c는 A가 채워질 수 있는 만큼 줌

        ####### C -> B
        if b + c <= B:
            if not visited[a][b + c]: # c의 물을 모두 b로 옮김
                visited[a][b + c] = True
                q.append((a, b + c, 0))
        else:
            if not visited[a][B]: 
                visited[a][B] = True
                q.append((a, B, c - (B - b))) # b가 B만큼 채워질 만큼 c를 줌

search()
print(*sorted(result))



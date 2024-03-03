'''
실버2. 랭킹전 대기열
https://www.acmicpc.net/problem/20006

1. 방이 없으면 새로운 방 생성
2. 이 방에 입장은 현재 들어온 레벨을 기준으로 -10 + 10

3. 방이 있다면 입장시킨 후 정뭔이 모두 차면 게임 시작
  - 방이 여러 개면 생성된 순으로 입장  

'''

import sys
from collections import deque

input = sys.stdin.readline

p, m = map(int, input().rstrip().split())
people = []
for _ in range(p):
    level, nickname = input().rstrip().split()
    people.append((int(level), nickname))
q = deque(people)

stack = []
room = []
while True:
    # 초기화 조건
    if len(room) == m:
        room = []
        q.extendleft(stack[::-1])
        stack = []
    
    # 종료 조건
    if not q and room:
        print('Waiting!')
        break
    elif not q and not room:
        break
        
    
    data = q.popleft()
    
    # 방이 생성 안되었으면    
    if not room:
        room.append(data)
    else:

        if room[0][0] - 10 <= data[0] <= room[0][0] + 10:
            room.append(data)
        else:
            stack.append(data)




'''
if room == 5:
    초기화
'''




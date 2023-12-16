'''
LV3. https://softeer.ai/practice/6289/history?questionType=ALGORITHM
'''

import sys

N, M = map(int, sys.stdin.readline().split())
list_w = list(map(int, sys.stdin.readline().split()))

# 자신이 최고 -> i번 회원이 연결된 j들 중에서 자신의 w가 가장 크면.
# 친분이 없는 멤버 -> 자기 자신

maps = [[] for i in range(N+1)]
for n in range(M):
  i, j = map(int, sys.stdin.readline().split())
  maps[i] += [j]
  maps[j] += [i]

# 본인 기준 
win = 0
for i in range(1, N+1):
  current = list_w[i-1]
  flag = False
  
  if not maps[i]:
    win += 1
    
  else:
    for rival in maps[i]:
      if current <= list_w[rival-1]:
        flag = True
        break
    if not flag:
      win += 1
      flag = False
      
print(win)
  
  
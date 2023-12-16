'''
LV3. https://softeer.ai/practice/6293
'''

import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

'''
3 2 1 5 4
1. 3
2. 2 : 3까지 최대 
3. 1 : 1이전까지 최대 + (자기자신이 가장 크면 + 1)
'''
result = [1] * N
for i in range(1, N):
  current_max = 0
  for j in range(i): # i이전까지 중 최대를 탐색하려고
    if data[i] > data[j]:
      current_max = max(current_max, result[j])
  result[i] = current_max + 1
print(max(result))
  
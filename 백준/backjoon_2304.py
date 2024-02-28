'''
실버2. https://www.acmicpc.net/problem/2304

벽면만 고려, x축은 자유롭게 이동이 가능함

- !!! 큰 기둥을 기준으로 나눠서 !!!
- 맨 처음이랑 끝은 무조건 벽 타야함.
- 다음 벽을 탈지, 그냥 이동할지 결정 기준
    - 현재 보다 높은 높이를 가지면 무조건 벽 타야함(그래야 포함)
'''

N = int(input())

data = [0 for _ in range(1001)]

best = 0
for i in range(N):
    L, H = map(int, input().split())
    data[L] = H
    if best < H:
        highest_idx = L
        best = H

# 왼쪽
left_max = 0
left = 0
for i in range(highest_idx+1):
    left_max = max(left_max, data[i])
    left += left_max
     
right_max = 0
right = 0
for i in range(1000, highest_idx, -1):
    right_max = max(right_max, data[i])
    right += right_max

print(left+right)
    





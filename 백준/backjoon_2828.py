import sys

input = sys.stdin.readline

N, M = map(int, input().split())
J = int(input())

left = 1
right = M
current = 1
total = 0
for _ in range(J):
    apple = int(input())

    # 범위 벗어나는 사과
    if left <= apple <= right:
        continue
    
    elif apple < left:
        diff = left - apple
        total += diff
        left -= diff
        right -= diff
    
    elif apple > right:
        diff = apple - right
        total += diff
        left += diff
        right += diff
    
print(total)
import sys

input = sys.stdin.readline

H, W = list(map(int, input().split()))
blocks = list(map(int, input().split()))

# 같거나 높은 높이의 블록이 나와야 함 -> 투 포인터로 

left, right = 0, W-1
left_m, right_m = blocks[left], blocks[right]

water = 0
while left < right: # 만나면 멈춰야지
    
    left_m, right_m = max(blocks[left], left_m), max(blocks[right], right_m) 

    if left_m < right_m: # 오른쪽이 더 높으면, 왼쪽 움직이면서 물 채우기
        water += (left_m - blocks[left]) # 현재 최고 높이 물 - 지금 높이
        left += 1
    else:
        water += (right_m - blocks[right]) # 현재 최고 높이 물 - 지금 높이
        right -= 1

print(water)


    
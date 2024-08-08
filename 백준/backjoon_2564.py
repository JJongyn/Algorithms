'''
https://www.acmicpc.net/problem/2564
'''

import sys

input = sys.stdin.readline

w, h = map(int, input().split())
k = int(input())

store = [list(map(int, input().split())) for _ in range(k)]
dong, dong_distance = list(map(int, input().split()))

result = 0
if dong == 1:
    for a, b in store:
        if a == 1: # 북
            result += abs(b-dong_distance)
        elif a == 2: # 남
            result += min(dong_distance + h + b, (w-dong_distance)+h+(w-b))
        elif a == 3: # 서
            result += dong_distance + b
        elif a == 4: # 동
            result += (w-dong_distance) + b

elif dong == 2:
    for a, b in store:
        if a == 1:
            result += min(dong_distance + h + b, (w-dong_distance)+h+(w-b))
        elif a == 2:
            result += abs(b-dong_distance)
        elif a == 3: # 서
            result += dong_distance + (h-b)
        elif a == 4: # 동
            result += (w-dong_distance) + (h-b)

elif dong == 3:
    for a, b in store:
        if a == 1:
            result += dong_distance + b
        elif a == 2:
            result += (h-dong_distance) + b
        elif a == 3:
            result += abs(b-dong_distance)
        elif a == 4:
            result += min(dong_distance+w+b, (h-dong_distance)+w+(h-b))

elif dong == 4:
    for a, b in store:
        if a == 1:
            result += dong_distance + (w-b)
        elif a == 2:
            result += (h-dong_distance) + (w-b)
        elif a == 3:
            result += min(dong_distance+w+b, (h-dong_distance)+w+(h-b))
        elif a == 4:
            result += abs(b-dong_distance)

print(result)
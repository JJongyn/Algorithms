import sys

def binary_search(array, target, start ,end):
    sol = 0
    while(start <= end):
        result = 0
        mid = (start + end) // 2                        # mid = 높이
        for i in array:
            if i > mid: result += i - mid
        if result < target:                             # 떡의 양이 부족할 경우 
            end = mid - 1
        else: 
            sol = mid
            start = mid + 1
    return sol


n, m = map(int, input().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))

print(binary_search(array, m, 0, max(array)))

import sys
import bisect

def cnt_binary_search(data, target):
    left_idx = bisect.bisect_left(data, target)
    right_idx = bisect.bisect_right(data, target)

    return right_idx - left_idx

N = int(sys.stdin.readline())
data = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))


for i in target:
    print(cnt_binary_search(data, i), end=' ')
    
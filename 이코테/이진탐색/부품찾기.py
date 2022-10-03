import sys

def binary_search(array, target, start, end):
    while(start <= end):
        mid = (start + end) // 2
        if array[mid] == target: return mid
        elif array[mid] > target: end = mid - 1
        else: start = mid + 1
    return None

n = int(input())
array = list(map(int, sys.stdin.readline().rstrip().split()))
array.sort()

m = int(input())
req = list(map(int, sys.stdin.readline().rstrip().split()))

result = []
for item in req:
    if binary_search(array, item, 0, len(array)-1):
        result.append("yes")
    else:result.append("no")

for i in result:
    print(i, end=' ')
import sys

input = sys.stdin.readline

n = int(input())
n_arr = sorted(list(map(int, input().split())))
m = int(input())
m_arr = list(map(int, input().split()))

def binary_search(target):
    start = 0
    end = len(n_arr) - 1
    
    while start <= end:
        mid = (start+end) // 2
        
        if n_arr[mid] == target:
            return 1
        elif n_arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for i in m_arr:
    print(binary_search(i))
    
import sys

input = sys.stdin.readline

N, S = map(int, input().split())
data = list(map(int, input().split()))

lst = []
cnt = 0

def search(st):
    global cnt
    if len(lst) > 0 and sum(lst) == S:
        cnt += 1
    
    for i in range(st, N):
        lst.append(data[i])
        search(i+1)
        lst.pop()

## main
search(0)
print(cnt)
    
import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))
data = sorted(list(map(int, input().split())))

dump = []
def search():
    if len(dump) == M:
        print(*dump)
        return
    
    for i in data:
        if i not in dump:
            dump.append(i)
            search()
            dump.pop()

search()
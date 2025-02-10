import sys

input = sys.stdin.readline

# 1 2 3 

def search(v, target):
    if eval(v) == target:
        results.append(v)
    if eval(v) > target:
        return
    search(f'{v}+1', target)
    search(f'{v}+2', target)
    search(f'{v}+3', target)

T = int(input())
for _ in range(T):
    target = int(input())
    results = []
    for i in ['1', '2', '3']:
        search(i, target)

    print(len({"+".join(sorted(result.split('+'))) for result in results}))      

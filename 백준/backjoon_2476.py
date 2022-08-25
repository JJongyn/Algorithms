import sys

n = sys.stdin.readline()
result = -sys.maxsize
for i in range(int(n)):
    a, b, c = map(int ,sys.stdin.readline().rstrip().split())
    if a == b == c:
        result = max(result, 10000 + a*1000)
    elif a == b:
        result = max(result, 1000+a*100)
    elif a == c:
        result = max(result, 1000+a*100)
    elif b == c:
        result = max(result, 1000+b*100)
    else:
        result = max(result, 100 * max(a,b,c))

print(result)
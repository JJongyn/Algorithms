
result = 0
current = 0
for _ in range(4):
    a, b = map(int, input().split())
    current += b
    current -= a
    result = max(result, current)
print(result)

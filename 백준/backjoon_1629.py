a, b, c = map(int, input().split())

# 0.5s
def solution(a, b, c):
    if b == 0:
        return 1
    x = solution(a, b//2, c)
    
    if b % 2 == 0:
        return x * x % c
    else:
        return x * x * a % c 

print(solution(a, b, c))
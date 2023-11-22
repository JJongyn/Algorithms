from collections import Counter

n = int(input())

# 적어도 1개만 입으면 나갈 수 있음
# 모든 경우의 수 - 전부 다 안 입는 경우


for _ in range(n):
    result = 1
    array = []
    m = int(input())
    for _ in range(m):
        a, t = input().split() # 옷 종류
        array.append(t)
    k = Counter(array)
    for i in k.keys():
        result *= k[i] + 1
    
    print(result - 1) # 전부 다 안입는 경우 빼기
    
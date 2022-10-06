

n = int(input())
array = [0] + list(map(int, input().split()))

d = [0] * 10001

for i in range(1, n + 1):
    for j in range(1, i + 1):
        d[i] = max(d[i], d[i-j]+array[j])
    
print(d[n])
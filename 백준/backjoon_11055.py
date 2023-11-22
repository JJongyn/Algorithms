n = int(input())
arr = list(map(int, input().split()))

d = arr[:]

for i in range(n):
    for j in range(0, i+1):
        if arr[i] > arr[j]:
            d[i] = max(d[i], d[j]+arr[i])

print(max(d))
n = int(input())
if n == 1:
    print(1)
else:
    data = [0 for i in range(n)]
    data[0] = 1
    data[1] = 3
    for i in range(2, n):
        data[i] = (data[i-1] + 2*data[i-2] ) % 10007

    print(data[n-1])
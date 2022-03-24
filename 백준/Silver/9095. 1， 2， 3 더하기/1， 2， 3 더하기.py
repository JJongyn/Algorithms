def count_sum(n):
    if n == 1:
        result = 1
    elif n == 2:
        result = 2
    else:
        d = [0 for i in range(n)]
        d[0] = 1
        d[1] = 2
        d[2] = 4
        for i in range(3, n):
            d[i] = (d[i - 1] + d[i - 2] + d[i - 3])

        result = d[n - 1]
    return result

n = int(input())
for i in range(n):
    print(count_sum(int(input())))




from itertools import combinations
while True:
    data = list(input().split())
    if len(data) == 1 and data[0] == '0':
        break
    a = combinations(data[1:], 6)
    for i in a:
        print(' '.join(i))
    print(' ')
    
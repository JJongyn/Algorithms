import sys

input = sys.stdin.readline

E, S, M = list(map(int, input().split()))

max_len = (15 * 28 * 19) + 1
for i in range(1, max_len):
    e = i % 15 if i % 15 > 0 else 15
    s = i % 28 if i % 28 > 0 else 28
    m = i % 19 if i % 19 > 0 else 19
        
    if E == e and S == s and M == m:
        print(i)
        break
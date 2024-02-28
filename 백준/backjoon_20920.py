'''
실버3. https://www.acmicpc.net/problem/20920
'''
import sys
from collections import Counter

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

data = {}
for _ in range(N):
    word = input().rstrip()
    if len(word) < M:
        continue
    else:
        if word not in data:
            data[word] = 1
        else:
            data[word] += 1
        
new_data = sorted(data.items(), key=lambda x: (-x[1], -len(x[0]), x[0])) # (x[1], len(x[0]), x[0])

for k in new_data:
    print(k[0])

        







        
        
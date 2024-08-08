'''
실버1. 문자열 교환

https://www.acmicpc.net/problem/1522

a는 모두 연속 <- 이를 위한 교환의 최소 회수
'''

import sys
from collections import Counter

input = sys.stdin.readline

word = input().rstrip()
sliding_len = Counter(word)['a']

def countVal(index):
    cnt = 0
    for i in range(index, index+sliding_len):
        if word[i % len(word)] == 'a':
           cnt += 1
    return cnt   

best = 100000        
for i in range(len(word)):
    best = min(best, sliding_len - countVal(i))
print(best)
        
        
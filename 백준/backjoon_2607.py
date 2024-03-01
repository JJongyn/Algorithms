'''
실버2. https://www.acmicpc.net/problem/2607
'''

import sys
input = sys.stdin.readline

N = int(input().rstrip())

data = [input().rstrip() for _ in range(N)]
target = data[0]
cnt = 0
for item in data[1:]:
    # 문자를 2개 처리해야하는 경우는 제외
    item = sorted(list(item))
    target = sorted(list(target))
    
    
    if abs(len(item) - len(target)) >= 2:
        continue
    
    # 길이가 같은 경우
    if len(item) == len(target):
        tmp = set(item) & set(target)
        if len(tmp) + 1 == len(set(item)) or len(tmp) == len(set(item)):
            cnt += 1
            
    # 길이가 1개 차이나는 경우
    else:
        tmp = set(item) & set(target)
        if len(tmp) == min(len(set(item)), len(set(target))):
            cnt+=1
            
print(cnt)
        
    

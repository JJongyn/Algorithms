'''
실버3. https://www.acmicpc.net/problem/19941
'''
import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split()) # K : 거리
data = list(input().rstrip())

# cnt = 0
# for i in range(len(data)):
#     if data[i] == 'P':
#         left = i - K
#         right = i + K + 1
#         for j in range(max(left, 0), min(right, N)):
#             if data[j] == 'H':
#                 cnt += 1
#                 data[j] = 0
#                 break
# print(cnt)

visited = [0 for _ in range(len(data))]

cnt = 0
for i in range(len(data)):
    if data[i] == 'P':
        left = i - K
        right = i + K + 1
        for j in range(max(left, 0), min(right, N)):
            if data[j] == 'H' and visited[j] == 0:
                cnt += 1
                visited[j] = 1
                break
print(cnt)
            
            
        
    
    
        


'''
240130
실버1. https://www.acmicpc.net/problem/12101

n, k
n을 1, 2, 3의 합으로 나타내는 방법
'''
n, k = map(int, input().split())


results = []
def back_tracking(ans):
    if sum(ans) > n:
        return 
    if sum(ans) == n:
        results.append(ans)
        return
    
    for i in range(1, 4):
        back_tracking(ans + [i])

back_tracking([])

if len(results) >= k and results[k-1]:
    print('+'.join(map(str, results[k-1])))
else:
    print(-1)
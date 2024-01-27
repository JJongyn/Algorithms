'''
실버1 https://www.acmicpc.net/problem/2529

'''


N = int(input())
data = list(input().split())

visited = [0] * 10
# min_ans = 
ans = []
def check(data1, data2, sign):
    if sign == '>':
        return int(data1) > int(data2)
    else:
        return int(data1) < int(data2)

def back_traking(start, results):
    if start == (N + 1):
        results = ''.join(results)
        ans.append(results)
        return
        # min_ans = min(int(results), min_ans)
        # max_ans = max(int(results), max_ans)
    
    for i in range(10):
        if visited[i] == 0:        
            if start == 0 or check(results[-1], i, data[start-1]):
                visited[i] = 1
                back_traking(start + 1, results + str(i))
                visited[i] = 0

back_traking(0, "")
print(max(ans))
print(min(ans))
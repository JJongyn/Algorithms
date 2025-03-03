import sys

input = sys.stdin.readline

k = int(input())
sign = list(input().split())

def check_sign(sign, num1, num2):
    if sign == '>':
        return int(num1) > int(num2)
    else:
        return int(num1) < int(num2)
    
data = []
ans = []
def search(depth):

    if len(data) == k+1:
        ans.append("".join(map(str, data)))
        return
    
    for i in range(10):
        if i not in data:
            if depth == 0 or check_sign(sign[depth-1], data[-1], i):
                data.append(i)
                search(depth+1)
                data.pop()
  
search(0)    
print(max(ans))
print(min(ans))    
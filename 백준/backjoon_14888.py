import sys

input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
sign = list(map(int, input().split())) # +, -, x, /

ans = []
def search(depth, num, plus, minus, multiply, devide):
    if depth == N:
        ans.append(num)
        return
    
    if plus:
        search(depth+1, num + data[depth], plus-1, minus, multiply, devide)
    if minus:
        search(depth+1, num - data[depth], plus, minus-1, multiply, devide)
    if multiply:
        search(depth+1, num * data[depth], plus, minus, multiply-1, devide)
    if devide:
        search(depth+1, int(num / data[depth]), plus, minus, multiply, devide-1)            

search(1, data[0], sign[0], sign[1], sign[2], sign[3])
print(max(ans))
print(min(ans))
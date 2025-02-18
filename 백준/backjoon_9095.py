import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    data = int(input())
    cnt = 0
    def search(_start, _sum):
        global cnt
        
        if _sum > data:
            return
        
        if _sum == data:
            cnt += 1
            return
        
        for i in range(1, 4):
            _sum += i
            search(_start, _sum)
            _sum -= i
            
    
    search(data, 0)
    print(cnt)
#from audioop import reverse
from collections import deque
import sys

N = int(sys.stdin.readline())

for i in range(N):
    function = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    data = sys.stdin.readline().rstrip()[1:-1].split(',')
    data = deque(data)

    reverse_cnt = 0
    err_flag = 0

    for j in function:
        if j == 'R':reverse_cnt += 1
        elif j =='D':
            if len(data) < 1 or n == 0:
                err_flag = 1
                print("error")
                break
            else:
                if reverse_cnt % 2 != 0: # 홀수면 맨 끝
                    data.pop()
                else:
                    data.popleft()
        
    if err_flag == 0:
        if reverse_cnt % 2 == 0: # 그냥 출력
            print("[" + ",".join(data) +"]")
        else:
            data.reverse()
            print("[" + ",".join(data) +"]")
    



import sys
import itertools

N = sys.stdin.readline().rstrip()

result = False
for i in range(len(N)):
    front_result = 1
    back_result = 1
    for j in N[0:i]:
        front_result *= int(j)
    for k in N[i:]:
        back_result *= int(k)
    if front_result == back_result:
        result = True
        break

if result and int(N) > 9:
    print("YES")
else:
    print("NO")

   
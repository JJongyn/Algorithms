import sys

# N % F == 0
N = int(sys.stdin.readline())
F = int(sys.stdin.readline())

# 뒤 두 자리 수만 바꾸기

rem = N % 100
if rem > 0:
    N = N - rem
    rem = 0

while (rem < 100):
    if (N + rem) % F == 0:
        break
    rem += 1

if rem < 10:
    print(str(rem).zfill(2))
else:
    print(rem)
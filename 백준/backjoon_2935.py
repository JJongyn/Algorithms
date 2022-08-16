import sys

a = sys.stdin.readline().rstrip()
op = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

if op == "*":
    print(int(a) * int(b))
else:
    print(int(a) + int(b))

        
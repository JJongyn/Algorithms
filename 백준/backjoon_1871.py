import sys

n = int(sys.stdin.readline())
data = [sys.stdin.readline().rstrip() for _ in range(n)]

for i in data:
    a = ord(i[0]) - 65
    b = ord(i[1]) - 65
    c = ord(i[2]) - 65
    alpha = (a * 26**2) + (b * 26**1) + c
    num = i[4:]
    if abs(int(alpha) - int(num)) <= 100:
        print("nice")
    else:
        print("not nice")
     



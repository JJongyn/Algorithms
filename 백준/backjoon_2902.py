import sys

name = sys.stdin.readline().rstrip()
print(name[0],end='')
for i in range(1, len(name)):
    if name[i] == '-':
        print(name[i+1],end='')
import sys

n = int(sys.stdin.readline())
data = sys.stdin.readline().rstrip().split()
data2 = set(data)
print(abs(len(data2)-len(data)))

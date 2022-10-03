import sys

n = int(input())
array = list(map(int, sys.stdin.readline().rstrip().split()))
array = set(array)

m = int(input())
req = list(map(int, sys.stdin.readline().rstrip().split()))

for item in req:
    if item in array:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
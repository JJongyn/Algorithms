import sys

N = int(sys.stdin.readline())
data = []
for i in range(N):
    data.append(list(sys.stdin.readline().strip()))
# print(data)
result = data[0]

for i in range(len(data)):
    if i != 0:
        for j in range(len(result)):
            if data[i][j] != result[j]:
                result [j] = "?"

result2 = ''.join(result)
print(result2)


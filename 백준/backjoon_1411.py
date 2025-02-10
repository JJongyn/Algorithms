import sys

input = sys.stdin.readline

N = int(input())
data = [input().strip() for _ in range(N)]

# 숫자로 바꾸기 
def change(num):
    dic = {}
    changed = ''
    for i in range(len(num)):
        if num[i] not in dic:
            dic[num[i]] = str(i)
            changed += str(i)
        else:
            changed += dic[num[i]]
    return changed

result = 0
for i in range(len(data)):
    for j in range(i+1, len(data)):
        word1, word2 = change(data[i]), change(data[j])
        result += 1 if word1 == word2 else 0

print(result)
        


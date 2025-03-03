import sys

input = sys.stdin.readline

N = int(input())

alphabets = [0 for _ in range(26)]
for i in range(N):
    word = input().rstrip()
    for j in range(len(word)):
        alphabets[ord(word[j]) - 65] += 10 ** (len(word) -j -1)

alphabets.sort(reverse=True)

ans = 0
num = 9
for i in range(len(alphabets)):
    if alphabets[i] == 0:
        break
    ans += alphabets[i] * num
    num -= 1

print(ans)
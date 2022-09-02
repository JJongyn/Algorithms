n = int(input())
for i in range(n):
    data = input()
    sq = str(pow(int(data),2))
    if sq[-len(data):] == data:print("YES")
    else:print("NO")
    
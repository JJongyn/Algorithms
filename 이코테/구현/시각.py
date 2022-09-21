n = int(input())

def count(data):
    if data == 3:
        return True

result = 0
for h in range(0, n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):     # 만약 23시11분11초면 231111로 만들어 줌
                result += 1
print(result)
# n = int(input())
# m = int(input())
# data = input()
# sol = 'I' + 'OI' * n

# result = 0
# for i in range(0, len(data) - len(sol) + 1):
#     if data[i] == 'I' and data[i:i+len(sol)] == sol:
#         result += 1

# print(result)

n = int(input())
m = int(input())
data = input()

i = 0
result = 0
data_cnt = 0
while i < m - 1: # 인덱스 범위를 넘으면 안되므로
    if data[i:i+3] == 'IOI': # IOIOI -> IOI가 2개
        i += 2 # 2칸씩 점프
        data_cnt += 1 # P에 따라서 연속된 IOI....OI가 결정되므로
        if data_cnt == n:
            result += 1
            data_cnt -= 1 # 위에서 나온 IOI..문자열의 마지막이 또다른 IOI와 이어질 수 있으므로
    else:
        i += 1
        data_cnt = 0
print(result)
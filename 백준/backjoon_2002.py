import sys

input = sys.stdin.readline

N = int(input())

# 입력
# car_in = [input().rstrip() for _ in range(N)]
# car_out = [input().rstrip() for _ in range(N)]

car_dic = {}
car_in, car_out = [], []
for i in range(N):
    car_num = input().rstrip()
    car_dic[car_num] = i
    car_in.append(i)

for _ in range(N):
    car_num = input().rstrip()
    car_out.append(car_dic[car_num])


'''
in: [0, 1, 2, 3]
out: [3, 0, 1, 2]

in: [0, 1, 2, 3, 4]
out: [1, 4, 3, 0, 2]
'''
result = 0
for i in range(N):
    if car_in[i] < car_out[i]:
        result += 1
    # elif car_in[i] == car_out[i]:
    #     if i != (N-1) and car_out[i] > car_out[i+1]:
    #         result += 1
print(result)


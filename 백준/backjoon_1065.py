# 각 자리가 등차수열을 이루는 수 찾기 -> 연속된 두 수의 차이가 일정
# 1 ~ 999 에서 한수의 개수를 출력 -> 완전 탐색

# 1 ~ 99 : 한수
# 100 ~ 999 : 가운데 숫자랑 뺀 절대값이 같으면 한수
n = int(input())

cnt = 0
for i in range(1, n+1):
    i_100_10 = (i // 100) - (i % 100) // 10 # i_100 = i / 100,  i_10 = (i % 100) / 10
    i_1_10 = (i % 100) // 10 - (i % 100) % 10
    if(i<100 or (i_100_10 == i_1_10)):cnt+=1
print(cnt)

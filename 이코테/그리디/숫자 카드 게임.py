N, M = map(int, input().split())

result = 0                                            # 결과값 초기화
for i in range(N):
    data = sorted(list(map(int, input().split())))    # 정렬을 통해 [0]이 최소가 되도록
    result = max(result, data[0])                     # 각 행끼리에서는 최대값을
print(result)

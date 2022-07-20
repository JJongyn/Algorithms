# 일곱 난쟁이의 키의 합이 100
# 입력이 크지 않음! -> 백트래킹, 완전 탐색이 사용될 수도 있음을 고려

## 입력 및 오름차순 ##
list = []
for i in range(9):
    list.append(int(input()))
list.sort()


## 키의 합이 100이 되는 인덱스 추출 ##
stop = True
for i in range(9):
    for j in range(9):
        if i != j:
            if(sum(list) - list[i] - list[j] == 100):
                stop = False
                break
    if(stop == False):break            

## 해당 인덱스 제외 출력 ## 
for k in range(9):
    if k == i or k == j:
        continue
    else:
        print(list[k])
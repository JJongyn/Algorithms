a1, b1 = map(int, input().split())
data1=[]
for _ in range(a1):
    data1.append(list(map(int, input().split())))
    

a2, b2 = map(int, input().split())
data2=[]
for _ in range(a2):
    data2.append(list(map(int, input().split())))      
    
result = [[0 for _ in range(b2)] for _ in range(a1)]

for i in range(a1):
    for k in range(b2):
        for j in range(b1):
            result[i][k] += data1[i][j] * data2[j][k]
            
for i in result:
    for j in i:
        print(j, end=' ')
    print()
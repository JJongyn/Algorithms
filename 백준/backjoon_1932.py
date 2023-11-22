n = int(input())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))
# print(array)    

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            array[i][j] = array[i][j] + array[i-1][j]
        elif i == j:
            array[i][j] = array[i][j] + array[i-1][j-1]
        else:
            array[i][j] = array[i][j] + max(array[i-1][j-1], array[i-1][j])
            
print(max(array[n-1])) 
        
    
    
    
# 0 -> 0, 1
# 1 -> 1, 2
# 2 -> 2, 3
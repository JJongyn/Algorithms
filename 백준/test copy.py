

a1, b1 = map(int, input().split())
data1=[]
for _ in range(a1):
    data1.append(list(map(int, input().split())))
    

a2, b2 = map(int, input().split())
data2=[]
for _ in range(a2):
    data2.append(list(map(int, input().split())))      
    
result = []    
for _ in range(a1):
    data = []
    for _ in range(b2):
        data.append(0)
    result.append(data)
    
result2 = [[0 for _ in range(b2)] for _ in range(a1)]

print(result)

print(result2)

result3 = [[0 for _ in range(b2)]for _ in range(a1)]

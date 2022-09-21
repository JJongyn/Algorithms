'''
L : 왼쪽으로 한 칸 이동
R : 오른쪽으로 한 칸 이동
U : 위쪽으로 한 칸 이동
D : 아래쪽으로 한 칸 이동
'''

n = int(input())
data = list(input().split())

loc_x = 1
loc_y = 1



move_x = [0, 0, 1, -1] # R, L, D, U
move_y = [1, -1, 0, 0]


move = ["R", "L", "D", "U"]

for m in data:
    for j in range(len(move)):
        if m == move[j]:
            
            dloc_x = loc_x + move_x[j]
            dloc_y = loc_y + move_y[j]
    

    if dloc_x < 1 or dloc_y < 1 or dloc_x > n or dloc_y > n:
        continue
        
    loc_x, loc_y = dloc_x, dloc_y
    
print(loc_x, loc_y)      
    

    
    
    
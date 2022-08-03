import sys

data = [0 for i in range(27)]
name = []
N = int(sys.stdin.readline())

for i in range(N):  
    name.append(sys.stdin.readline())

for i in range(len(name)):
    data[ord(name[i][0])-97]+=1
    #data[name[i][0] - 97] += 1

flag = 0
for i in range(27):
    if data[i] >= 5:
        print(chr(i+97),end='')
        flag = 1
if flag==0 :print("PREDAJA")


    


## 소수 집합 만들어놓기 ##
is_prime = [True] * 1000001

for i in range(2, int(1000001**(0.5))+1):
    if is_prime[i]:
        for j in range(i*i, 1000001, i):        
            is_prime[j] = False
 
while True:
    data = int(input())
    
    if data == 0:
        break
    
    # b-a가 가장 크다 -> a가 가장 작은 수, b가 그럼 큰 수
    for a in range(3, int(len(is_prime) / 2) + 1):
        b = data - a
        
        if is_prime[a] and is_prime[b]:
            print(f"{data} = {a} + {b}")
            break
    else:
        print("Goldbach's conjecture is wrong.")
            
        
                
        
    
    
    
import sys

input = sys.stdin.readline

word = input().rstrip()

first = {
    1:'I',
    2:'II',
    3:'III',
    4:'IV',
    5:'V',
    6:'VI',
    7:'VII',
    8:'VIII',
    9:'IX'
}

second = {
    10:'X',
    20:'XX',
    30:'XXX',
    40:'XL',
    50:'L',
    60:'LX',
    70:'LXX',
    80:'LXXX',
    90:'XC'
}

for i in range(1, 100):
    if i < 10:
        ones = i % 10
        new_word = first[ones]
    else:
        tens = (i // 10) * 10
        ones = i % 10
        
        if ones == 0:
            new_word = second[tens]
        else:
            new_word = second[tens] + first[ones]
        
    
    if sorted(word) == sorted(new_word):
        print(new_word)
        break
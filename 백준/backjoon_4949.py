'''
실버4. https://www.acmicpc.net/problem/4949

'''

while True:
    numbers = list(input())
    stack = []
    if len(numbers) == 1 and numbers[0] == '.':
        break
        
    for num in numbers:
        if num == '(' or num == '[':
            stack.append(num)
        elif num == ')' and stack and stack[-1] == '(':
            stack.pop()
        elif num == ']' and stack and stack[-1] == '[':
            stack.pop()
        elif num == ']' or num == ')':
            stack.append(num)
    if stack:
        print("no")
    else:
        print("yes")
'''
실버4. https://www.acmicpc.net/problem/9012

6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(

3
((
))
())(()
'''

N = int(input())
for _ in range(N):
    stack = []
    numbers = list(input())
    for num in numbers:
        if num == '(' or num == '[':
            stack.append(num)
        elif num == ')' and stack and stack[-1] == '(':
            stack.pop()
        elif num == ']' and stack and stack[-1] == '[':
            stack.pop()
        elif num == ']' or num == '[':
            stack.append(num)
    print(stack)
    if stack:
        print("NO")
    else:
        print("YES")
# N = int(input())

# for _ in range(N):
#     s = input().strip()
    
#     while '()' in s:
#         s = s.replace('()', ' ')
#     if s:
#         print('NO')
#     else:
#         print('YES')


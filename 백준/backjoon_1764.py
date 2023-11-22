n, m = map(int, input().split())

n_arr = [input() for i in range(n)]
m_arr = [input() for i in range(m)]

result = list(set(n_arr) & set(m_arr))
print(len(result))
for i in sorted(result):
    print(i)
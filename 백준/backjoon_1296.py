import sys


def getScore(name_data, team_data):

    L = name_data.count("L") + team_data.count("L")
    O = name_data.count("O") + team_data.count("O")
    V = name_data.count("V") + team_data.count("V")
    E = name_data.count("E") + team_data.count("E")

    return ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100

   

name = sys.stdin.readline()
n = int(sys.stdin.readline())

result = -sys.maxsize - 1

for i in range(n):
    data = sys.stdin.readline()
    max_result = getScore(name, data)

    if max_result == result and data_result > data:
        data_result = data

    elif max_result > result:
        result = max_result
        data_result = data

print(data_result)
    



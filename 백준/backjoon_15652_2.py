import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
def search(start):
    
    if len(graph) == M:
        print(*graph)
        return
    
    for i in range(start, N+1):
        graph.append(i)
        search(i)
        graph.pop()

search(1)
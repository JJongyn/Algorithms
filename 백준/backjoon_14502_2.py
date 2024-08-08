import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


def search():
    
'''
실버3. https://www.acmicpc.net/problem/17484
'''
import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))
    
    

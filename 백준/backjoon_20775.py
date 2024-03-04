'''
실버2. https://www.acmicpc.net/problem/2075
'''

import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []
for _ in range(N):
    numbers = map(int, input().split())
    for number in numbers:
        if len(heap) < N:
            heapq.heappush(heap, number) # N 보다 작으면 힙을 N개로 만들어주려구
        else:
            if heap[0] < number: # 최소힙이니깐 가장 작은 수보다 현재값이 더 크면
                heapq.heappop(heap)
                heapq.heappush(heap, number)
print(heap[0])
        



'''
Heap의 자료구조 특성 상 N개를 유지하면 이것이 정렬되서 유지.
N개를 유지하면서 가장 작은 값(루트)를 현재값과 비교해주면 최종적으로는 가장 큰 N개만 남을 것이고
이중에서 루트값은 N개중 가장 작은 값임
'''






    
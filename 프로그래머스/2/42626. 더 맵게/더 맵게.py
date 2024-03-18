from heapq import *


def solution(scovill, K):
    heap = []
    result = 0
    for i in scovill:
        heappush(heap, i)
    while heap[0] < K and len(heap) >= 2:
        first = heappop(heap)
        second = heappop(heap)
        heappush(heap, first + second * 2)
        result += 1
    if heap[0] < K:
        return -1
    return result

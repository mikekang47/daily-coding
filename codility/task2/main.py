from collections import deque

def solution(A: list, K: int):
    d = deque(A)
    d.rotate(K)
    return list(d)

A = [3,8,9,7,6]
K = 3
solution(A,K)
from collections import defaultdict

def solution(A):
    d = defaultdict(int)
    for i in A:
        d[i] += 1
    for i in d.keys():
        if d[i] % 2 != 0:
            return i

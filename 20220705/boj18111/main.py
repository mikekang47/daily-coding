import sys

input = sys.stdin.readline
N, M, B = map(int, input().split())
L = [0 for i in range(257)]
for _ in range(N):
    for i in map(int, input().split()):
        L[i] = L[i] + 1
        B = B + i

t_min = N * M * 512
for h in range(1 + B // (N * M)):
    t = sum(map(lambda x, i: 2 * i * x, L[h:], range(len(L) - h)))
    t += sum(map(lambda x, i: 1 * i * x, L[0:h], range(h, 0, -1)))
    if t_min >= t: t_min, H_min = t, h
print(t_min, H_min)

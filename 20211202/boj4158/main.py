import sys

while 1:
    n, m = map(int, sys.stdin.readline().strip().split())
    if n == 0 and m == 0:
        break
    sang = set()
    sun = set()
    for _ in range(n):
        sang.add(int(sys.stdin.readline()))
    for _ in range(m):
        sun.add(int(sys.stdin.readline()))
    print(len(sang.intersection(sun)))

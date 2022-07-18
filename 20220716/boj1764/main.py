import sys
n, m = map(int, sys.stdin.readline().split())
li = sys.stdin.read().split()
i = sorted(set(li[:n]) & set(li[n:]))
print(len(i), *i, sep="\n")






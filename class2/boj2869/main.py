import sys

a, b, v = map(int, sys.stdin.readline().split())
# k일까지 올라간 거리 = (k-1)*(a-b) + a = -> k(a-b) + b = v
print((v-b-1) // (a-b) + 1)



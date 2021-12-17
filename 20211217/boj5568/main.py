import itertools
import sys
n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
dic = {}
num = [str(input()) for i in range(n)]
print(len(set(list(map(''.join, itertools.permutations(num, k))))))


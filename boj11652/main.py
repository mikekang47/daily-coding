from collections import defaultdict
import sys
n = int(sys.stdin.readline())
dic = defaultdict(int)
for i in range(n):
    temp = int(sys.stdin.readline())
    dic[temp] += 1

result = sorted(dic.keys(), key=lambda x: (-dic[x], x))
print(result[0])

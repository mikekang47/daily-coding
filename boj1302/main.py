from collections import defaultdict

n = int(input())
li = [input() for _ in range(n)]
dic = defaultdict()
for i in set(li):
    dic[i] = li.count(i)
keys = sorted(list(dic.keys()), key=lambda x: (-dic[x], x))
print(keys[0])

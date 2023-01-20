from collections import defaultdict

n, c = map(int, input().split())
a = list(input().split())

dic = defaultdict(int)
for i in a:
    dic[i] += 1

arr = sorted(dic.items(), reverse=True, key=lambda x: x[1])
s = ""
for i in arr:
    s += (i[0] + " ") * i[1]

print(s)

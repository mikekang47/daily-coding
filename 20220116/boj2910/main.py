from collections import defaultdict

n, c = map(int, input().split())
l = input().split()
cnt = {}

for i in l:
    if cnt.get(i) == None:
        cnt[i] = 1
    else:
        cnt[i] += 1

ans = sorted(cnt.items(), reverse=True, key=lambda x:x[1])

string = ''
for i in ans:
    string += (i[0]+" ") * i[1]

print(string)

















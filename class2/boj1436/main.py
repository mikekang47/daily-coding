import re

n = int(input())
s = "666"
temp = ""
r = re.compile("666[^0]?")
li = []
i = 0
while len(li) <= 10000:
    if r.findall(str(i)):
        li.append(i)
    i += 1
print(sorted(li)[n-1])
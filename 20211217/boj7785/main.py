import sys
p = int(sys.stdin.readline().strip())
dic = {}
for i in range(p):
    name, status = sys.stdin.readline().strip().split()
    dic[name] = status
person = []
for i in list(dic.keys()):
    if dic[i] == "enter":
        person.append(i)
person.sort(reverse=True)
for i in person:
    print(i)
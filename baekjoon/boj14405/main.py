li = ["pi","ka","chu"]
n = input()
for i in li:
    n = n.replace(i, "")

if len(n) == 0:
    print("YES")
else:
    print("NO")
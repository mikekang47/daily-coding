n = int(input())
li = sorted([input() for _ in range(n)], key=lambda x: (int(x.split()[0]), int(x.split()[1])))
for i in li:
    print(i)
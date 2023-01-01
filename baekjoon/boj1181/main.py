n = int(input())
li = list(set([input() for _ in range(n)]))
li.sort(key=lambda x:(len(x),x))
for i in li:
    print(i)
x, y, w, h = map(int, input().split())
li = []
li.append(h-y)
li.append(w-x)
li.append(x)
li.append(y)
print(min(li))

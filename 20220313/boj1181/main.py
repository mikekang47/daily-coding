arr = list(set(input() for _ in range(int(input()))))
arr.sort()
arr.sort(key=len)
for x in arr:
    print(x)
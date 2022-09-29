n = int(input())
li = set(list(map(int, input().split())))
m = int(input())
arr = list(map(int, input().split()))
for i in arr:
    if i in li:
        print("1")
    else:
        print("0")
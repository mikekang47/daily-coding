k = int(input())
arr = []
for i in range(k):
    temp = int(input())
    if temp == 0:
        arr.pop(-1)
    else:
        arr.append(temp)
print(sum(arr))
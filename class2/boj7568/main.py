n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
arr = [0 for _ in range(n)]
for i in range(n):
    arr[i] = len(list(filter(lambda x: x[0] > li[i][0] and x[1] > li[i][1], li)))
s = ""
for i in arr:
    s += str(i +1) + " "
print(s.strip())


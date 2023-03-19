n = int(input())
for i in range(n):
    li = list(map(int, input().split()))
    li.sort()
    print(li[-3])
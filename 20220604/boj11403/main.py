n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            a[i][j] |= a[i][k] and a[k][j]
for x in a:
    for y in x:
        print(y,end=' ')
    print()



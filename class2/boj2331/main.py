n = int(input())
for i in range(1, n):
    if i + sum(map(int, str(i))) == n:
        print(i)
        exit(0)
print(0)

row, col, mx = 0, 0, 0

for i in range(9):
    arr = list(input().split())
    a = max(arr)
    if mx < int(a):
        mx = int(a)
        row = i+1
        col = arr.index(a) + 1

print(mx)
print(row, col)


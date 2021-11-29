import sys

n, m = map(int, input().split())
books = []
if n == 0:
    print(0)
    sys.exit()
st = list(input().split())
for i in st:
    books.append(int(i))
temp = 0
cnt = 0
while books:
    if temp + books[0] <= m:
        temp += books[0]
        books.pop(0)
    else:
        cnt += 1
        temp = 0
cnt += 1
print(cnt)
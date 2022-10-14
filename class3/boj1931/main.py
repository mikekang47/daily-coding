n = int(input())
li = [tuple(map(int, input().split())) for _ in range(n)]
li.sort(key=lambda x: (x[1], x[0]))
cnt = 1
t1, t2 = li[0][0], li[0][1]
li.pop(0)
for a, b in li:
    if t2 <= a:
        t2 = b
        cnt += 1
print(cnt)

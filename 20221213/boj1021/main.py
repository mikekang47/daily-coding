from collections import deque

n, m = map(int, input().split())
d = [i for i in range(1, n + 1)]
d = deque(d)
li = list(map(int, input().split()))

cnt = 0
for i in li:
    if d[0] == i:
        d.popleft()
    else:
        leftArray = d.copy()
        rightArray = d.copy()
        right, left = 0, 0
        while leftArray[0] != i:
            leftArray.rotate(-1)
            left += 1
        while rightArray[0] != i:
            rightArray.rotate(1)
            right += 1
        cnt += min(right, left)

        d = leftArray
        d.popleft()
print(cnt)

s = input()
k = int(input())
start = s[:k]
if start == s[-k:]:
    print(0)
else:
    cnt = 0
    print(start)
    print(s[-k:])
    for i, j in zip(start, s[-k:]):
        if i != j:
            cnt += 1

    print(cnt)

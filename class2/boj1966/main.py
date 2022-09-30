t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    arr = list(enumerate(li))
    cnt = 1
    while 1:
        if max(li) == arr[0][1]:
            if arr[0][0] == m:
                print(cnt)
                break
            else:
                cnt += 1
                arr.pop(0)
                li.remove(max(li))
        elif max(li) != arr[0][1]:
            arr.append(arr.pop(0))










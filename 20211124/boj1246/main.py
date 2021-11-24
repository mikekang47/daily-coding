n, m = map(int, input().split())
wantToPay = []
for i in range(m):
    wantToPay.append(int(input()))
wantToPay.sort()
dict = {}
for i in range(len(wantToPay)):
    if len(wantToPay[i:]) > n:
        dict[n * wantToPay[i]] = wantToPay[i]
    else:
        dict[len(wantToPay[i:]) * wantToPay[i]] = wantToPay[i]
p = max(dict.keys())
print(dict[p], p)

import sys
n,m = map(int, sys.stdin.readline().rstrip().split())
li = [False for _ in range(m - n + 1)]
cnt = 0
for i in range(2, int(m**0.5)+1):
    po = i ** 2
    start_index = n // po
    if n % po != 0:
        start_index += 1
    for j in range(start_index, m // po + 1):
        if not li[j * po - n]:
            li[j * po - n] = True
            
for i in range(m - n + 1):
    if not li[i]:
        cnt += 1
print(cnt)

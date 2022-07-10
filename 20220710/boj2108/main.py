import statistics

n = int(input())
li = [int(input()) for _ in range(n)]
li.sort()
print(round(statistics.mean(li)))
print(int(statistics.median(li)))
if len(statistics.multimode(li)) >= 2:
    print(statistics.multimode(li)[1])
else:
    print(print(statistics.multimode(li)[0]))
print(li[-1] - li[0])
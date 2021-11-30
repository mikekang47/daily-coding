n, s, r = map(int, input().split())
broken = list(map(int, input().split()))
rest = list(map(int, input().split()))

result_rest = set(rest) - set(broken)
result_broken = set(broken) - set(rest)

for i in result_rest:
    if (i - 1) in result_broken:
        result_broken.remove(i-1)
    elif (i + 1) in result_broken:
        result_broken.remove(i+1)
print(len(result_broken))

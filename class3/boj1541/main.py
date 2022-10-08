a = [sum(map(int, x.split('+'))) for x in input().split('-')]
print(a[0] - sum(a[1:]))

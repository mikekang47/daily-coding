li = [sum(map(int, x.split("+"))) for x in input().split("-")]
print(li[0] - sum(li[1:]))
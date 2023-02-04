n = int(input())
li = [input().split() for _ in range(n)]
li.sort(key=lambda x: (-int(x[3]), -int(x[2]), -int(x[1])))
print(li[0][0])
print(li[-1][0])

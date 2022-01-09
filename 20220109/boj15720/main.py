b,c,d = map(int, input().split())
burger = sorted(list(map(int, input().split())), reverse=True)
side = sorted(list(map(int, input().split())), reverse=True)
beverage = sorted(list(map(int, input().split())), reverse=True)

total = sum(burger) + sum(side) + sum(beverage)

minV = min(b,c,d)

cost = 0

for _  in range(minV):
    cost += (burger[0] + side[0] + beverage[0]) * 0.9
    burger.pop(0)
    side.pop(0)
    beverage.pop(0)

for i in range(len(burger)):
    cost += burger[i]
for i in range(len(side)):
    cost += side[i]
for i in range(len(beverage)):
    cost += beverage[i]

print(total)
print(int(cost))


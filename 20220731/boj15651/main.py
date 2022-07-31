from itertools import product

n, m = map(int, input().split())
# r = [perm for perm in list(permutations(range(1, n+1), m)) if sorted(perm) == list(perm)]

for i in list(product(range(1, n+1), repeat=m)):
    for j in range(m):
        print(i[j], end = ' ')
    print()
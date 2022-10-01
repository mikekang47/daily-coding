N, M, B = map(int, input().split())
blocks = []
for _ in range(N):
    blocks.extend(list(map(int, input().split())))
max_height = (sum(blocks) + B) // (N * M)
if max_height > 256: max_height = 256
bf = [0 for _ in range(max_height + 1)]
min_val, height = float('inf'), -1
for idx in range(max_height + 1):
    for i in blocks:
        if i > idx:
            bf[idx] += 2 * (i - idx)
        else:
            bf[idx] += idx - i
    if min_val >= bf[idx]:
        min_val = bf[idx]
        height = idx
print(min_val, height)

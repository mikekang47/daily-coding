import sys
n = int(sys.stdin.readline())
li = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
li.sort(key=lambda x: (x[1], x[0]))
result = 1
end = li[0][1]
li.pop(0)
for i,j  in li:
    if end <= i:
        end = j
        result += 1
print(result)

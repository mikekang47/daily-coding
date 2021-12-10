import sys
square = [1, 1]
n = int(sys.stdin.readline().strip())
for i in range(2, n):
    square.append(square[i-2] + square[i-1])

if n == 1:
    print(4)
    sys.exit()
width = square[-1]+square[-2]
high = square[-1]
print(width * 2 + high * 2)

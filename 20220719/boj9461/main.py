
n = int(input())
for _ in range(n):
    triangle = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    p = int(input())
    if p <= 10:
        print(triangle[p])
    else:
        for i in range(11, p+1):
            triangle.append(triangle[i-1] + triangle[i-5])
        print(triangle[p])

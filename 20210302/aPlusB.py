a = int(input())
for i in range(1,a+1):
    b,c = input().split()
    b = int(b)
    c = int(c)
    print("Case #%d: %d + %d = %d" %(i, b, c, b+ c))
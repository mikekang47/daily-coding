start = 666
n = int(input())
while 1:
    if str(start).find("666") != -1:
        n -= 1
    if n == 0:
        break
    start += 1
print(start)


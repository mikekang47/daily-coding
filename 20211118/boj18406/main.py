n = str(input())
if sum(map(int, n[:int(len(n)/2)])) == sum(map(int, n[int(len(n)/2):])):
    print("LUCKY")
else:
    print("READY")


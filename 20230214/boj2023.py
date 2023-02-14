n = int(input())

def isPrime(n) :
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

queue = [2,3,5,7]
if n == 1:
    print(*queue)
    exit()

while len(str(queue[0])) != n:
    temp = queue.pop(0)
    for i in range(temp*10, (temp+1)*10):
        if isPrime(i):
            queue.append(i)

print(*queue)


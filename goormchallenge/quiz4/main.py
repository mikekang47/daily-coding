import math
import sys


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
result = 0
for i in range(len(li)):
    if isPrime(i+1):
        result += li[i]
print(result)

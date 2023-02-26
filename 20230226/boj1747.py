import sys
import math

n = int(sys.stdin.readline().rstrip())
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

    
for i in range(n, 2000000):
    if isPrime(i) and str(i) == str(i)[::-1]:
        print(i)
        break
import math
import decimal
import sys

n, m = map(int, sys.stdin.readline().split())
print(decimal.Decimal(math.factorial(n) // (math.factorial(n - m) * math.factorial(m))))

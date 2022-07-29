import math
import decimal
n, m = map(int, input().split())
print(decimal.Decimal(math.factorial(n) // (math.factorial(n-m) *  math.factorial(m))))
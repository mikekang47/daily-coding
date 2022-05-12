import sys

l = int(input())
s = list(map(int, input().split()))
n = int(input())

s.append(0)
s.sort()

a = 0

for i in range(len(s)-1):
    if s[i] == n or s[i+1] == n:
        a = 0
        break
    elif s[i] < n < s[i + 1]:
        a = (n-s[i]) * (s[i+1]-n) - 1
        break

print(a)

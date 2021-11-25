import sys

s = str(input().split('.'))
arr = []
temp = ""
while len(s):
    if len(s) >= 4:
        s = s[:4]
        arr.append("AAAA")
    elif len(s) >= 2:
        s = s[:2]
        arr.append("BB")
    elif
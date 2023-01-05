import re

regex = re.compile('(pi|ka|chu)*')
n = input()

if re.fullmatch(regex, n):
    print("YES")
else:
    print("NO")
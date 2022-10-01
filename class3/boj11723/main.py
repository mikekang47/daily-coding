import sys

n = int(sys.stdin.readline())
a = set()
for _ in range(n):
    s = list(sys.stdin.readline().split())
    if len(s) == 2:
        command = s[0]
        value = int(s[1])
        if command == "add":
            a.add(value)
        elif command == "remove":
            a.remove(value) if value in a else None
        elif command == "check":
            print(1 if value in a else 0)
        elif command == "toggle":
            a.remove(value) if value in a else a.add(value)
    else:
        command = s[0]
        if command == "all":
            a = set(range(1, 21))
        elif command == "empty":
            a = set()

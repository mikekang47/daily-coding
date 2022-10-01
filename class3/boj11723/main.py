n = int(input())
sets = set()
for _ in range(n):
    s = list(input().split())
    command = s[0]
    if command == "add":
        sets.add(s[1])
    elif command == "remove":
        if s[1] in sets:
            sets.remove(s[1])
    elif command == "check":
        print(1 if s[1] in sets else 0)
    elif command == "toggle":
        if s[1] in sets:
            sets.remove(s[1])
        else:
            sets.add(s[1])
    elif command == "all":
        sets = set(i for i in range(1, 21))
    elif command == "empty":
        sets = set()


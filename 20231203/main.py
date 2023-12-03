import sys

n = int(sys.stdin.readline())
li = []
while n > 0 :
    commands = list(map(int, sys.stdin.readline().rstrip().split()))
    command = commands[0]

    if command == 1:
        li.append(commands[1])
    elif command == 2:
        if len(li) != 0:
            print(li.pop())
        else:
            print(-1)
    elif command == 3:
        print(len(li))
    elif command == 4:
        if len(li) == 0:
            print(1)
        else:
            print(0)
    elif command == 5:
        if len(li) != 0:
            print(li[-1])
        else:
            print(-1)
    n -= 1

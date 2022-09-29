import sys

t = int(sys.stdin.readline())
st = []
for _ in range(t):
    command = sys.stdin.readline()
    if command.split()[0] == "push":
        st.append(command.split()[1])
    elif command.split()[0] == "pop":
        if len(st) == 0:
            print(-1)
        else:
            print(st.pop())
    elif command.split()[0] == "size":
        print(len(st))
    elif command.split()[0] == "empty":
        if len(st) == 0:
            print(1)
        else:
            print(0)
    elif command.split()[0] == "top":
        if len(st) == 0:
            print(-1)
        else:
            print(st[-1])



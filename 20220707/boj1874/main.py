import sys
n = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(n)]
st = []
char = []
flag = 0
for i in range(1, n+1):
    st.append(i)
    char.append('+')
    while len(st) != 0:
        if li[0] == st[-1]:
            st.pop(-1)
            li.pop(0)
            char.append('-')
        else:
            break


if len(st) != 0:
    print("NO")
else:
    for i in char:
        print(i)








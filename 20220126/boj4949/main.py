while 1:
    line = input()
    if line == '.':
        break
    st = []
    for i in line:
        if i == '(' or i == ')' or i == '[' or i == ']':
            if len(st) == 0:
                st.append(i)
            elif st[-1] == '(' and i == ')':
                st.pop()
            elif st[-1] == '[' and i == ']':
                st.pop()
            else:
                st.append(i)
    if len(st) == 0:
        print("yes")
    else:
        print("no")





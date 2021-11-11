s = list(str(input()))
one = []
zero = []
temp = s[0]
for i in range(1, len(s)):
    if s[i] == temp[-1]:
        temp += s[i]
    else:
        if temp[-1] == '0':
            zero.append(temp)
        else:
            one.append(temp)
        temp = s[i]

if temp[-1] == '0':
    zero.append(temp)
else:
    one.append(temp)

if len(one) > len(zero):
    print(len(zero))
else:
    print(len(one))

